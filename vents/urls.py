from django.urls import path, include
from .views import (
    VentDetailView,
    VentListView,
    login, logout
)


urlpatterns = [
    #path('logout/', logout, name='logout'),
    #path('login/', login, name = 'login'),
    path('', VentListView.as_view(), name = 'list'),
    path('<int:pk>/', VentDetailView.as_view(), name = 'detail'),

    #path('rest-auth/', include('rest_auth.urls')),
]