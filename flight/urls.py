from importlib.resources import path
from rest_framework import routers
from flight.views import FlightView, ReservationView
from django.urls import path, include

router = routers.DefaultRouter()
router.register('flights', FlightView)
router.register('resv', ReservationView)

urlpatterns = [
    # path('', include(router.urls)),
]

urlpatterns += router.urls