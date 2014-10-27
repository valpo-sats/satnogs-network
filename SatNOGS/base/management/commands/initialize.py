from orbit import satellite

from django.core.management.base import BaseCommand

from base.tests import ObservationFactory, StationFactory
from base.models import Satellite


class Command(BaseCommand):
    help = 'Create initial fixtures'

    def handle(self, *args, **options):
        ObservationFactory.create_batch(200)
        StationFactory.create_batch(200)

        satellites = Satellite.objects.all()

        for obj in satellites:
            try:
                sat = satellite(obj.norad_cat_id)
            except:
                self.stdout.write(('Satellite {} with Identifier {} does '
                                  'not exist [deleted]').format(obj.name, obj.norad_cat_id))
                obj.delete()
                continue

            obj.name = sat.name()
            tle = sat.tle()
            obj.tle0 = tle[0]
            obj.tle1 = tle[1]
            obj.tle2 = tle[2]
            obj.save()
            self.stdout.write(('Satellite {} with Identifier {} '
                              'found [updated]').format(obj.norad_cat_id, obj.name))
