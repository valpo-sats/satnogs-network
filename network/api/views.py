from django.utils.timezone import now

import django_filters
from rest_framework import viewsets, mixins

from network.api.perms import StationOwnerCanEditPermission
from network.api import serializers
from network.base.models import (Antenna, Data, Observation, Satellite,
                                 Station, Transponder)


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


class DataFilter(django_filters.FilterSet):
    class Meta:
        model = Data
        fields = ['start', 'end', 'ground_station']


class DataView(viewsets.ReadOnlyModelViewSet, mixins.UpdateModelMixin):
    queryset = Data.objects.all()
    serializer_class = serializers.DataSerializer
    filter_class = DataFilter
    permission_classes = [
        StationOwnerCanEditPermission
    ]

    def get_queryset(self):
        payload = self.request.QUERY_PARAMS.get('payload', None)
        if payload == '':
            return self.queryset.filter(payload='')
        return super(DataView, self).get_queryset()


class JobView(viewsets.ReadOnlyModelViewSet):
    queryset = Data.objects.filter(payload='')
    serializer_class = serializers.JobSerializer
    filter_class = DataFilter
    filter_fields = ('ground_station')

    def get_queryset(self):
        return self.queryset.filter(start__gte=now())
