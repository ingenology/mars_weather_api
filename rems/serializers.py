from .models import Report, Status

from rest_framework import serializers


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    max_temp_fahrenheit = serializers.FloatField(source='max_temp_fahrenheit')
    min_temp_fahrenheit = serializers.FloatField(source='min_temp_fahrenheit')

    class Meta:
        model = Report
        fields = (
            'terrestrial_date',
            'sol',
            'ls',
            'min_temp',
            'min_temp_fahrenheit',
            'max_temp',
            'max_temp_fahrenheit',
            'pressure',
            'pressure_string',
            'abs_humidity',
            'wind_speed',
            'wind_direction',
            'atmo_opacity',
            'season',
            'sunrise',
            'sunset',
            )

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('status_text', 'start_date', 'end_date', )

