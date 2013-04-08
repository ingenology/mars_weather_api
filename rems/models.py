from django.db import models


class Report(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    terrestrial_date = models.DateTimeField()
    sol = models.IntegerField(verbose_name="Sol Number")
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

    def __unicode__(self):
        return self.terrestrial_date.strftime('%Y%m%d')
