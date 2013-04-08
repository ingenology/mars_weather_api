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
    # TODO THIS IS WRONG....
    date_str = dt.strftime('%Y%m%d')
    return parse("{} {}".format(date_str, time), fuzzy=True)


def process_report(report):
    "Take report data and return Report kwargs"
    tdate = parse(report.get('terrestrial_date'), fuzzy=True)
    sol = report.get('sol')
    mags = report['magnitudes']
    return {
        'sol': sol,
        'terrestrial_date': tdate,
        'min_temp': float_or_none(mags.get('min_temp')),
        'max_temp': float_or_none(mags.get('max_temp')),
        'pressure': float_or_none(mags.get('pressure')),
        'pressure_string': mags.get('pressure_string'),
        'abs_humidity': float_or_none(mags.get('abs_humidity')),
        'wind_speed': float_or_none(mags.get('wind_speed')),
        'wind_direction': mags.get('wind_direction'),
        'atmo_opacity': mags.get('atmo_opacity'),
        'season': mags.get('season'),
        'ls': float_or_none(mags.get('ls')),
        'sunrise': time_to_datetime(tdate, mags.get('sunrise')),
        'sunset': time_to_datetime(tdate, mags.get('sunset')),
    }


def fetch_report():
    "Fetch new report from cab.inta-csic.es"
    rems_url = 'http://cab.inta-csic.es/rems/rems_weather.xml'
    resp = requests.get(rems_url)
    data = xmltodict.parse(resp.content)

    # TODO check date
    # what do we compare here???

    report = data['weather_report']
    kwargs = process_report(report)
    Report.objects.create(**kwargs)


def import_marsweather():
    "Import history from marsweather.com"
    marsweather_archive = 'http://data.marsweather.com/rems_climate.xml'
    resp = requests.get(marsweather_archive)
    data = xmltodict.parse(resp.content)

    reports = data['climate_report']['record']

    for report in reports:
        Report.objects.create(**process_report(report))
