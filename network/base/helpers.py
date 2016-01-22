from network.base.models import Satellite, Tle


def get_latest_tle(satellite):
    latest_tle = Tle.objects.filter(satellite=satellite).latest('updated')
    return latest_tle
