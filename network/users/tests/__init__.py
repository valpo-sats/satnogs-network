import datetime
import factory

from factory import fuzzy

from network.users.models import User


def int2roman(n):
    roman_map = (('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
                 ('C', 100), ('XC', 90), ('L', 50), ('XL', 40), ('X', 10),
                 ('IX', 9), ('V', 5), ('IV', 4), ('I', 1))

    if not (0 < n < 5000):
        raise Exception('Out of range error.')
    result = ''
    for numeral, integer in roman_map:
        while n >= integer:
            result += numeral
            n -= integer
    return result


class UserFactory(factory.django.DjangoModelFactory):
    """User model factory."""
    username = factory.Sequence(lambda n: 'username%s' % n)
    first_name = 'John'
    last_name = factory.Sequence(lambda n: 'Doe %s' % int2roman(n))
    email = factory.LazyAttribute(lambda o: '%s@example.com' % o.username)
    password = factory.PostGenerationMethodCall('set_password', 'passwd')
    is_staff = False
    is_active = True
    is_superuser = False
    last_login = datetime.datetime(2012, 1, 1)
    date_joined = datetime.datetime(2011, 1, 1)
    bio = fuzzy.FuzzyText()

    class Meta:
        model = User
