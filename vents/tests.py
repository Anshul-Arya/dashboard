from django.test import TestCase
from .models import Vent_Availability
from rest_framework.test import APITestCase, APIRequestFactory
from vents import views

# Create your tests here.

class ModelTestCase(TestCase):
    """This class defines the test suite for the Vent_Availability model."""
    def setUp(self):
        Vent_Availability.objects.create(FacilityName = "Test Facility",
                                         Tier = 1, Region = 'Region 1',
                                         Group = 'Test', lat = 30.000012,
                                         lng = '-30.00045', Total_Vents = 15,
                                         Available_Vents = 0,
                                         Predicted_Vent_Shortage_in_14days = 15)
        Vent_Availability.objects.create(FacilityName="Test Facility 2",
                                         Tier=2, Region='Region 2',
                                         Group='Test 1', lat=35.000012,
                                         lng='-35.00045', Total_Vents=16,
                                         Available_Vents=1,
                                         Predicted_Vent_Shortage_in_14days=15)

    def test_vent_shortage(self):
        vent_1 = Vent_Availability.objects.get(id=1)
        field_value = vent_1._meta.get_field('FacilityName').verbose_name
        self.assertEqual(field_value,'FacilityName')


class TestVent(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.VentListView.as_view({'get': 'list'})
        self.uri = '/api/v1/'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))