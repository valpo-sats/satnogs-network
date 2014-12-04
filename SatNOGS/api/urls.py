from django.conf.urls import patterns, url, include
from rest_framework import routers

from api import views


router = routers.DefaultRouter()

router.register(r'antennas', views.AntennaView)
router.register(r'data', views.DataView)
router.register(r'observations', views.ObservationView)
router.register(r'satellites', views.SatelliteView)
router.register(r'stations', views.StationView)
router.register(r'transponders', views.TransponderView)

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls))
)
