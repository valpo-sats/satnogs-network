import signal
import sys
from optparse import make_option
from orbit import satellite

from django.core.management.base import BaseCommand, CommandError

from base.models import Satellite


def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--delete',
                    action='store_true',
                    dest='delete',
                    default=False,
                    help='Delete Satellites'),
    )
    args = '<Satellite Range>'
    help = 'Updates/Inserts TLEs for a range of Satellites (eg. xxxx:xxxx)'

    def handle(self, *args, **options):
        for arg in args:
            try:
                start, end = arg.split(':')
            except ValueError:
                raise CommandError('You need to spacify the range in the form: xxxx:xxxx')

        r = range(int(start), int(end))
        for item in r:
            if options['delete']:
                try:
                    Satellite.objects.get(norad_cat_id=item).delete()
                    self.stdout.write('Satellite {}: deleted'.format(item))
                    continue
                except:
                    self.stdout.write('Satellite with Identifier {} does not exist'.format(item))
                    continue

            try:
                sat = satellite(item)
            except:
                self.stdout.write('Satellite with Identifier {} does not exist'.format(item))
                continue

            try:
                obj = Satellite.objects.get(norad_cat_id=item)
            except:
                obj = Satellite(norad_cat_id=item)

            obj.name = sat.name()
            obj.save()

            self.stdout.write('fetched data for {}: {}'.format(obj.norad_cat_id, obj.name))
