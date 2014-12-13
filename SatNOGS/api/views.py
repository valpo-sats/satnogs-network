from rest_framework import viewsets, mixins

from api.perms import StationOwnerCanEditPermission
from api import serializers
from base.models import (Antenna, Data, Observation, Satellite, Station,
                         Transponder)


class AntennaView(viewsets.ModelViewSet):
    queryset = Antenna.objects.all()
    serializer_class = serializers.AntennaSerializer


class StationView(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = serializers.StationSerializer


class SatelliteView(viewsets.ModelViewSet):
    queryset = Satellite.objects.all()
    serializer_class = serializers.SatelliteSerializer


class TransponderView(viewsets.ModelViewSet):
    queryset = Transponder.objects.all()
    serializer_class = serializers.TransponderSerializer


class ObservationView(viewsets.ModelViewSet):
    queryset = Observation.objects.all()
    serializer_class = serializers.ObservationSerializer


class DataView(viewsets.ReadOnlyModelViewSet,
               mixins.UpdateModelMixin):
    queryset = Data.objects.all()
    serializer_class = serializers.DataSerializer
    permission_classes = [
        StationOwnerCanEditPermission
    ]
