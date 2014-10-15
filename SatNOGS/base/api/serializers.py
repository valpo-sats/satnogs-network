from rest_framework import serializers

from base.models import (Antenna, Data, Observation, Satellite, Station,
                         Transponder)


class AntennaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Antenna
        fields = ('frequency', 'band', 'antenna_type')


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('owner', 'name', 'image', 'alt', 'lat', 'lng',
                  'antenna', 'featured', 'featured_date')


class SatelliteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Satellite
        fields = ('norad_cat_id', 'name')


class TransponderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transponder
        fields = ('description', 'alive', 'uplink_low', 'uplink_high',
                  'downlink_low', 'downlink_high', 'mode', 'invert',
                  'baud', 'satellite')


class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = ('satellite', 'transponder', 'author', 'start', 'end')


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('start', 'end', 'observation', 'ground_station', 'payload')
