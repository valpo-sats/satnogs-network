import ephem
from datetime import datetime, timedelta

from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now
from django.http import JsonResponse

from .models import Station, Transponder, Observation, Data, Satellite


def index(request):
    """View to render index page."""
    observations = Observation.objects.all()
    featured_stations = Station.objects.filter(featured=True)

    ctx = {
        'latest_observations': observations.filter(end__lt=now()),
        'scheduled_observations': observations.filter(end__gte=now()),
        'featured_station': featured_stations.latest('featured_date')
    }

    return render(request, 'base/home.html', ctx)


def observations_list(request):
    """View to render Observations page."""
    observations = Observation.objects.all()

    return render(request, 'base/observations.html', {'observations': observations})


def observation_new(request):
    """View for new observation"""
    satellites = Satellite.objects.all()
    transponders = Transponder.objects.filter(alive=True)

    return render(request, 'base/observation_new.html', {'satellites': satellites,
                                                         'transponders': transponders})


def prediction_windows(request, sat_id, start_date, end_date):
    sat = get_object_or_404(Satellite, norad_cat_id=sat_id)
    satellite = ephem.readtle(str(sat.tle0), str(sat.tle1), str(sat.tle2))

    end_date = datetime.strptime(end_date, '%Y-%m-%d %H:%M')

    data = []

    stations = Station.objects.all()
    for station in stations:
        observer = ephem.Observer()
        observer.lon = str(station.lng)
        observer.lat = str(station.lat)
        observer.elevation = station.alt
        observer.date = str(start_date)
        station_match = False
        keep_digging = True
        while keep_digging:
            tr, azr, tt, altt, ts, azs = observer.next_pass(satellite)

            if ephem.Date(tr).datetime() < end_date:
                if not station_match:
                    station_windows = {
                        'id': station.id,
                        'name': station.name,
                        'window': []
                    }
                    station_match = True

                if ephem.Date(ts).datetime() > end_date:
                    ts = end_date
                    keep_digging = False
                else:
                    time_start_new = ephem.Date(ts).datetime() + timedelta(minutes=1)
                    observer.date = time_start_new.strftime("%Y-%m-%d %H:%M:%S.%f")

                station_windows['window'].append(
                    {
                        'start': ephem.Date(tr).datetime().strftime("%Y-%m-%d %H:%M:%S.%f"),
                        'end': ephem.Date(ts).datetime().strftime("%Y-%m-%d %H:%M:%S.%f"),
                        'az_start': azr
                    })

            else:
                # window start outside of window bounds
                break

        if station_match:
            data.append(station_windows)

    return JsonResponse(data, safe=False)


def view_observation(request, id):
    """View for single observation page."""
    observation = get_object_or_404(Observation, id=id)
    data = Data.objects.filter(observation=observation)

    return render(request, 'base/observation_view.html',
                  {'observation': observation, 'data': data})
