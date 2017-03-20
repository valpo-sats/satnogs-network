import math
from datetime import timedelta
from rest_framework.authtoken.models import Token


def get_apikey(user):
    try:
        token = Token.objects.get(user=user)
    except:
        token = Token.objects.create(user=user)
    return token


def calculate_polar_data(observer, satellite, start, end, points):
    observer = observer.copy()
    satellite = satellite.copy()
    duration = (start - end).total_seconds()
    delta = duration / points
    temp_date = start
    data = []
    while temp_date < end:
        observer.date = temp_date
        satellite.compute(observer)
        data.append([float(format(math.degrees(satellite.alt), '.4f')),
                     float(format(math.degrees(satellite.az), '.4f'))])
        temp_date = temp_date - timedelta(seconds=delta)
    temp_date = end
    observer.date = temp_date
    satellite.compute(observer)
    data.append([float(format(math.degrees(satellite.alt), '.4f')),
                 float(format(math.degrees(satellite.az), '.4f'))])
    return data


def resolve_overlaps(station, gs_data, start, end):
    if gs_data:
        for datum in gs_data:
            if datum.is_past:
                continue
            if datum.start <= end and start <= datum.end:
                if datum.start <= start and datum.end >= end:
                    return False
                if start < datum.start and end > datum.end:
                    start1 = start
                    end1 = datum.start
                    start2 = datum.end
                    end2 = end
                    return start1, end1, start2, end2
                if datum.start <= start:
                    start = datum.end
                if datum.end >= end:
                    end = datum.start
    return start, end
