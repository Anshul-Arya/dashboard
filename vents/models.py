from django.db import models

# Create your models here.
class Vent_Availability(models.Model):
    FacilityName = models.CharField(max_length=100)
    Tier = models.IntegerField()
    Region = models.CharField(max_length=100)
    Group = models.CharField(max_length=100)
    lat = models.FloatField(verbose_name='Lat', null=True, blank=True)
    lng = models.FloatField(verbose_name='Long', null=True, blank=True)
    Total_Vents = models.IntegerField()
    Available_Vents = models.IntegerField()
    Predicted_Vent_Shortage_in_14days = models.IntegerField()

    def __str__(self):
        return self.FacilityName

    class Meta:
        db_table = 'veny_availability'
        verbose_name = 'Vent_Availability'
        verbose_name_plural = 'Vent_Availabilities'
