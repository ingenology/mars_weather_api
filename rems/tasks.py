import re
import requests
import xmltodict

from dateutil.parser import parse

from .models import Report


def float_or_none(val):
    "Handle weird non-float values. i.e. '--' == None"
    try:
        return float(val)
    except ValueError:
        return None

def time_to_datetime(dt, time):
    "Convert '6 am' to a datetime on tdate"
    if not time:
        return None
    date_str = dt.strftime('%Y%m%d')
    return parse("{} {}".format(date_str, time), fuzzy=True)


def parse_date(date_string):
    return parse(date_string, fuzzy=True).date()


def create_or_update_report(data):
    sol = data.get('sol')
    tdate = parse_date(data['terrestrial_date'])

    # see if report for sol exists (sol is unique)
    # if it does exist, check date and return if no update
    try:
        report = Report.objects.get(sol=sol)
    except Report.DoesNotExist:
        report = Report(sol=sol)
    else:
        if tdate <= report.terrestrial_date:
            return None

    mags = data['magnitudes']

    report.sol = sol
    report.terrestrial_date = tdate
    report.min_temp = float_or_none(mags.get('min_temp'))
    report.max_temp = float_or_none(mags.get('max_temp'))
    report.pressure = float_or_none(mags.get('pressure'))
    report.pressure_string = mags.get('pressure_string')
    report.abs_humidity = float_or_none(mags.get('abs_humidity'))
    report.wind_speed = float_or_none(mags.get('wind_speed'))
    report.wind_direction = mags.get('wind_direction')
    report.atmo_opacity = mags.get('atmo_opacity')
    report.season = mags.get('season')
    report.ls = float_or_none(mags.get('ls'))
    report.sunrise = time_to_datetime(tdate, mags.get('sunrise'))
    report.sunset = time_to_datetime(tdate, mags.get('sunset'))

    report.save()
    return report


def fetch_report():
    "Fetch new report from cab.inta-csic.es"
    rems_url = 'http://cab.inta-csic.es/rems/rems_weather.xml'
    resp = requests.get(rems_url)
    data = xmltodict.parse(resp.content)
    report_data = data['weather_report']
    return create_or_update_report(report_data)


def import_marsweather():
    "Import history from marsweather.com"
    marsweather_archive = 'http://data.marsweather.com/rems_climate.xml'
    resp = requests.get(marsweather_archive)
    data = xmltodict.parse(resp.content)

    records = data['climate_report']['record']

    for report_data in records:
        # The marsweather.com data has "Ene"/Enero instead "Jan"/January
        # so we have to check for that first
        tdate = report_data.get(u'terrestrial_date')
        ene_pattern = re.compile(r'(.*)[Ee]ne')
        if ene_pattern.match(tdate):
            report_data['terrestrial_date'] = ene_pattern.sub('Jan', tdate)

        # we also don't trust their sunrise and sunset times
        report_data['magnitudes']['sunrise'] = None
        report_data['magnitudes']['sunset'] = None

        create_or_update_report(report_data)
