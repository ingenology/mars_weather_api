from .models import Report

from rest_framework import serializers


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Report
        fields = (
            'terrestrial_date',
            'sol',
            'ls',
            'min_temp',
            'max_temp',
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

