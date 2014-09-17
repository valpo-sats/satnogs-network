# -*- coding: utf-8 -*-
from django.contrib import admin

from base.models import Antenna, Satellite, Station, Transponder, Observation


class AntennaAdmin(admin.ModelAdmin):
    list_display = ('antenna_type', 'frequency', 'band')


class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'lng', 'lat')


class SatelliteAdmin(admin.ModelAdmin):
    list_display = ('name', 'norad_cat_id')


class TransponderAdmin(admin.ModelAdmin):
    list_display = ('satellite', 'description', 'uplink_low', 'uplink_high', 'downlink_low', 'downlink_high')

admin.site.register(Antenna, AntennaAdmin)
admin.site.register(Satellite, SatelliteAdmin)
admin.site.register(Station, StationAdmin)
admin.site.register(Transponder, TransponderAdmin)
admin.site.register(Observation)
