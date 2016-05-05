import django_filters

from network.base.models import Data


class DataViewFilter(django_filters.FilterSet):
    start = django_filters.IsoDateTimeFilter(name='start', lookup_type='gte')

    class Meta:
        model = Data
        fields = ['ground_station', 'start']
