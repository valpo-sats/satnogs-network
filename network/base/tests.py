import random
from datetime import datetime, timedelta

import factory
from factory import fuzzy
from django.utils.timezone import now

from network.base.models import (ANTENNA_BANDS, ANTENNA_TYPES, RIG_TYPES, OBSERVATION_STATUSES,
                                 Rig, Mode, Antenna, Satellite, Station, Transmitter, Observation,
                                 Data, DemodData)
from network.users.tests import UserFactory


def generate_payload():
    payload = '{0:b}'.format(random.randint(500000000, 510000000))
    digits = 1824
    while digits:
        digit = random.randint(0, 1)
        payload += str(digit)
        digits -= 1
    return payload


def generate_payload_name():
    filename = datetime.strftime(fuzzy.FuzzyDateTime(now() - timedelta(days=10), now()).fuzz(),
                                 '%Y%m%dT%H%M%SZ')
    return filename


def get_valid_satellites():
    qs = Transmitter.objects.all()
    satellites = Satellite.objects.filter(transmitters__in=qs).distinct()
    return satellites


class RigFactory(factory.django.DjangoModelFactory):
    """Rig model factory."""
    name = fuzzy.FuzzyChoice(choices=RIG_TYPES)
    rictld_number = fuzzy.FuzzyInteger(1, 3)

    class Meta:
        model = Rig


class ModeFactory(factory.django.DjangoModelFactory):
    """Mode model factory."""
    name = fuzzy.FuzzyText()

    class Meta:
        model = Mode


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
    featured_date = fuzzy.FuzzyDateTime(now() - timedelta(days=10), now())
    active = fuzzy.FuzzyChoice(choices=[True, False])
    last_seen = fuzzy.FuzzyDateTime(now() - timedelta(days=3), now())
    horizon = fuzzy.FuzzyInteger(10, 20)
    rig = factory.SubFactory(RigFactory)

    @factory.post_generation
    def antennas(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for antenna in extracted:
                if random.randint(0, 1):
                    self.antenna.add(antenna)

    class Meta:
        model = Station


class SatelliteFactory(factory.django.DjangoModelFactory):
    """Sattelite model factory."""
    norad_cat_id = fuzzy.FuzzyInteger(2000, 4000)
    name = fuzzy.FuzzyText()

    class Meta:
        model = Satellite


class TransmitterFactory(factory.django.DjangoModelFactory):
    """Transmitter model factory."""
    description = fuzzy.FuzzyText()
    alive = fuzzy.FuzzyChoice(choices=[True, False])
    uplink_low = fuzzy.FuzzyInteger(200000000, 500000000, step=10000)
    uplink_high = fuzzy.FuzzyInteger(200000000, 500000000, step=10000)
    downlink_low = fuzzy.FuzzyInteger(200000000, 500000000, step=10000)
    downlink_high = fuzzy.FuzzyInteger(200000000, 500000000, step=10000)
    mode = factory.SubFactory(ModeFactory)
    invert = fuzzy.FuzzyChoice(choices=[True, False])
    baud = fuzzy.FuzzyInteger(4000, 22000, step=1000)
    satellite = factory.SubFactory(SatelliteFactory)

    class Meta:
        model = Transmitter


class ObservationFactory(factory.django.DjangoModelFactory):
    """Observation model factory."""
    satellite = factory.Iterator(get_valid_satellites())
    author = factory.SubFactory(UserFactory)
    start = fuzzy.FuzzyDateTime(now() - timedelta(days=3),
                                now() + timedelta(days=3))
    end = factory.LazyAttribute(
        lambda x: x.start + timedelta(hours=random.randint(1, 8))
    )

    @factory.lazy_attribute
    def transmitter(self):
        return self.satellite.transmitters.all().order_by('?')[0]

    class Meta:
        model = Observation


class DataFactory(factory.django.DjangoModelFactory):
    start = fuzzy.FuzzyDateTime(now() - timedelta(days=3),
                                now() + timedelta(days=3))
    end = factory.LazyAttribute(
        lambda x: x.start + timedelta(minutes=random.randint(1, 20))
    )
    observation = factory.SubFactory(ObservationFactory)
    ground_station = factory.Iterator(Station.objects.all())
    payload = factory.django.FileField(filename='data.ogg')
    vetted_datetime = factory.LazyAttribute(
        lambda x: x.end + timedelta(hours=random.randint(1, 20))
    )
    vetted_user = factory.SubFactory(UserFactory)
    vetted_status = fuzzy.FuzzyChoice(choices=OBSERVATION_STATUSES)

    class Meta:
        model = Data


class DemodDataFactory(factory.django.DjangoModelFactory):
    data = factory.Iterator(Data.objects.all())
    payload_demod = factory.django.FileField()

    class Meta:
        model = DemodData
