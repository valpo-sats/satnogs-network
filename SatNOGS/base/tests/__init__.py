import factory
import random

from datetime import timedelta
from django.utils.timezone import now
from factory import fuzzy

from base.models import (ANTENNA_BANDS, ANTENNA_TYPES, MODE_CHOICES,
                         Antenna, Satellite, Station, Transponder, Observation)
from users.tests import UserFactory


class AntennaFactory(factory.django.DjangoModelFactory):
    """Antenna model factory."""
    frequency = fuzzy.FuzzyFloat(200, 500)
    band = fuzzy.FuzzyChoice(choices=ANTENNA_BANDS)
    antenna_type = fuzzy.FuzzyChoice(choices=ANTENNA_TYPES)

    class Meta:
        model = Antenna


class StationFactory(factory.django.DjangoModelFactory):
    """Station model factory."""
    owner = factory.SubFactory(UserFactory)
    name = fuzzy.FuzzyText()
    image = factory.django.ImageField()
    alt = fuzzy.FuzzyInteger(0, 800)
    lat = fuzzy.FuzzyFloat(-20, 70)
    lng = fuzzy.FuzzyFloat(-180, 180)
    featured = fuzzy.FuzzyChoice(choices=[True, False])

    @factory.post_generation
    def antennas(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for antenna in extracted:
                self.antenna.add(antenna)

    class Meta:
        model = Station


class SatelliteFactory(factory.django.DjangoModelFactory):
    """Sattelite model factory."""
    norad_cat_id = fuzzy.FuzzyInteger(1000, 8000)
    name = fuzzy.FuzzyText()
    tle = fuzzy.FuzzyText()
    updated = fuzzy.FuzzyDateTime(now() - timedelta(days=3),
                                now() + timedelta(days=3))

    class Meta:
        model = Satellite


class TransponderFactory(factory.django.DjangoModelFactory):
    """Transponder model factory."""
    description = fuzzy.FuzzyText()
    alive = fuzzy.FuzzyChoice(choices=[True, False])
    uplink_low = fuzzy.FuzzyInteger(200, 500)
    uplink_high = fuzzy.FuzzyInteger(200, 500)
    downlink_low = fuzzy.FuzzyInteger(200, 500)
    downlink_high = fuzzy.FuzzyInteger(200, 500)
    mode = fuzzy.FuzzyChoice(choices=MODE_CHOICES)
    invert = fuzzy.FuzzyChoice(choices=[True, False])
    baud = fuzzy.FuzzyInteger(4000, 22000, step=1000)
    satellite = factory.SubFactory(SatelliteFactory)

    class Meta:
        model = Transponder


class ObservationFactory(factory.django.DjangoModelFactory):
    """Observation model factory."""
    satellite = factory.SubFactory(SatelliteFactory)
    author = factory.SubFactory(UserFactory)
    start = fuzzy.FuzzyDateTime(now() - timedelta(days=3),
                                now() + timedelta(days=3))
    end = factory.LazyAttribute(
        lambda x: x.start + timedelta(hours=random.randint(1, 8))
    )
    transponder = factory.SubFactory(TransponderFactory)

    class Meta:
        model = Observation
