from django.shortcuts import render
from django.utils.timezone import now
from django.core import serializers

from django.http import HttpResponse


from base.models import Station, Observation


def index(request):
    """View to render index page."""
    observations = Observation.objects.all()
    stations = Station.objects.all()

    ctx = {
        'latest_observations': observations.filter(end__lt=now()),
        'scheduled_observations': observations.filter(end__gte=now()),
        'stations': stations
    }

    return render(request, 'base/home.html', ctx)


def stations_json(request):
    data = serializers.serialize('json', Station.objects.all())

    return HttpResponse(data, content_type='application/json')
