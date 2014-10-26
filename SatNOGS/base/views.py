import ephem
from datetime import datetime, timedelta

from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now
from django.http import JsonResponse

from .models import Station, Observation, Data, Satellite


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


def prediction_windows(request, sat_id, start_date, end_date):
    sat = get_object_or_404(Satellite, norad_cat_id=sat_id)
    satellite = ephem.readtle(str(sat.tle0), str(sat.tle1), str(sat.tle2))

    end_date = datetime.strptime(end_date, '%Y-%m-%d %H:%M')

    data = {'windows': []}

    stations = Station.objects.all()
    for station in stations:
        observer = ephem.Observer()
        observer.lon = str(station.lng)
        observer.lat = str(station.lat)
        observer.elevation = station.alt
        observer.date = str(start_date)
        station_match = False
        while True:
            satellite.compute(observer)
            window = observer.next_pass(satellite)

            if not _check_window_sanity(window):
                window_new = list(window)
                window_new[0] = window[4]  # replace 0 with 4
                window_new[1] = window[1]
                window_new[2] = window[2]
                window_new[3] = window[3]
                window_new[4] = window[0]  # replace 4 with 0
                window_new[5] = window[5]
                window = window_new

            if ephem.Date(window[0]).datetime() < end_date:
                if not station_match:
                    station_windows = {
                        'station_id': station.id,
                        'station_name': station.name,
                        'window': []
                    }
                    station_match = True
                station_windows['window'].append(
                    {
                        'start': ephem.Date(window[0]).datetime().strftime("%Y-%m-%d %H:%M:%S.%f"),
                        'end': ephem.Date(window[4]).datetime().strftime("%Y-%m-%d %H:%M:%S.%f"),
                        'az_start': window[1]
                    })
                if ephem.Date(window[4]).datetime() > end_date:
                    # window end outside of window bounds; break
                    break
                else:
                    time_start_new = ephem.Date(window[4]).datetime() + timedelta(seconds=1)
                    observer.date = time_start_new.strftime("%Y-%m-%d %H:%M:%S.%f")
            else:
                # window start outside of window bounds
                break

        if station_match:
            data['windows'].append(station_windows)

    return JsonResponse(data)


def _check_window_sanity(window):
    """
    Weird bug in ephem library's next_pass function
    returns set time earlier than rise time, leads to infinite loop
    """
    if ephem.Date(window[0]).datetime() > ephem.Date(window[4]).datetime():
        return False
    return True


def view_observation(request, id):
    """View for single observation page."""
    observation = get_object_or_404(Observation, id=id)
    data = Data.objects.filter(observation=observation)

    return render(request, 'base/observation_view.html',
                  {'observation': observation, 'data': data})
