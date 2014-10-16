from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now
from django.core import serializers

from django.http import HttpResponse


from base.models import Station, Observation, Data


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


def stations_json(request):
    data = serializers.serialize('json', Station.objects.all())

    return HttpResponse(data, content_type='application/json')


def view_observation(request, id):
    """View for single observation page."""
    observation = get_object_or_404(Observation, id=id)
    data = Data.objects.filter(observation=observation)

    return render(request, 'base/observation_view.html',
                  {'observation': observation, 'data': data})
