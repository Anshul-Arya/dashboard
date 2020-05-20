from rest_framework import generics
from vents.models import Vent_Availability
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework import (
    filters,
    permissions,
    viewsets,
    status
)
from .serializers import VentSerializer

@csrf_exempt
@api_view(["POST"])
@permission_classes((permissions.IsAuthenticated,))
def logout(request):
    request.user.auth_token.delete()
    return Response(status=HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username is None or password is None:
        return Response({'error': 'Please Provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


class VentListView(generics.ListCreateAPIView):
#class VentListView(viewsets.ModelViewSet):
    queryset = Vent_Availability.objects.all().order_by('Region')
    serializer_class = VentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields =['FacilityName', 'Region']
    lookup_field = 'FacilityName'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #authentication_classes = (TokenAuthentication,)



class VentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vent_Availability.objects.all()
    serializer_class = VentSerializer
    permission_classes = [permissions.IsAuthenticated]
    #authentication_classes = (TokenAuthentication,)

