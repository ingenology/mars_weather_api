from django.db import models

from .utils import celsius_to_fahrenheit


class Report(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    terrestrial_date = models.DateField()
    sol = models.IntegerField(verbose_name="Curiosity Sol Number", unique=True)
    ls = models.FloatField(blank=True, null=True, verbose_name="Seasonal Date")

    min_temp = models.FloatField(blank=True, null=True)
    max_temp = models.FloatField(blank=True, null=True)
    pressure = models.FloatField(blank=True, null=True)
    pressure_string = models.CharField(max_length=255, blank=True)
    abs_humidity = models.FloatField(blank=True, null=True)
    wind_speed = models.FloatField(blank=True, null=True)
    wind_direction = models.CharField(max_length=255, blank=True, null=True)
    atmo_opacity = models.CharField(max_length=255, blank=True, null=True)
    season = models.CharField(max_length=255, blank=True)

    sunrise = models.DateTimeField(blank=True, null=True)
    sunset = models.DateTimeField(blank=True, null=True, help_text="It's blue")

    class Meta:
        ordering = ('-sol', )
        get_latest_by = ('sol', )

    def __unicode__(self):
        return self.terrestrial_date.strftime('%Y%m%d')

    @property
    def min_temp_fahrenheit(self):
        return celsius_to_fahrenheit(self.min_temp)

    @property
    def max_temp_fahrenheit(self):
        return celsius_to_fahrenheit(self.max_temp)
