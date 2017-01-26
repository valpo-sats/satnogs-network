from rest_framework import serializers

from network.base.models import Data, Station, DemodData


class DemodDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemodData
        fields = ('payload_demod', )


class DataSerializer(serializers.ModelSerializer):
    transmitter = serializers.SerializerMethodField()
    norad_cat_id = serializers.SerializerMethodField()
    demoddata = DemodDataSerializer(many=True)

    class Meta:
        model = Data
        fields = ('id', 'start', 'end', 'observation', 'ground_station', 'transmitter',
                  'norad_cat_id', 'payload', 'waterfall', 'demoddata')
        read_only_fields = ['id', 'start', 'end', 'observation', 'ground_station',
                            'transmitter', 'norad_cat_id']

    def update(self, instance, validated_data):
        demod_data = validated_data.pop('demoddata')
        data = super(DataSerializer, self).update(instance, validated_data)
        for demod in demod_data:
            data.demoddata.create(payload_demod=demod['payload_demod'])
        return data

    def get_transmitter(self, obj):
        try:
            return obj.observation.transmitter.uuid
        except AttributeError:
            return ''

    def get_norad_cat_id(self, obj):
        return obj.observation.satellite.norad_cat_id


class JobSerializer(serializers.ModelSerializer):
    frequency = serializers.SerializerMethodField()
    tle0 = serializers.SerializerMethodField()
    tle1 = serializers.SerializerMethodField()
    tle2 = serializers.SerializerMethodField()
    mode = serializers.SerializerMethodField()

    class Meta:
        model = Data
        fields = ('id', 'start', 'end', 'ground_station', 'tle0', 'tle1', 'tle2',
                  'frequency', 'mode')

    def get_frequency(self, obj):
        return obj.observation.transmitter.downlink_low

    def get_tle0(self, obj):
        return obj.observation.tle.tle0

    def get_tle1(self, obj):
        return obj.observation.tle.tle1

    def get_tle2(self, obj):
        return obj.observation.tle.tle2

    def get_mode(self, obj):
        try:
            return obj.observation.transmitter.mode.name
        except:
            return ''


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('uuid', 'name', 'alt', 'lat', 'lng', 'rig',
                  'active', 'antenna', 'id', 'apikey')

    apikey = serializers.CharField(read_only=True)
