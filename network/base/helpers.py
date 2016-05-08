import random
from datetime import timedelta, datetime

from django.utils.timezone import now
from factory import fuzzy
from rest_framework.authtoken.models import Token


def get_apikey(user):
    try:
        token = Token.objects.get(user=user)
    except:
        token = Token.objects.create(user=user)
    return token


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
