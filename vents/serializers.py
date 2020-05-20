from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Vent_Availability


class VentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vent_Availability
        fields= ('id', 'FacilityName',
                 'Tier', 'Region', 'Group',
                 'lat', 'lng', 'Total_Vents',
                 'Available_Vents', 'Predicted_Vent_Shortage_in_14days')

