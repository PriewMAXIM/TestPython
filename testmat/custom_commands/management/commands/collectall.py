from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.conf import settings
import time
import os
from subprocess import call

class Command(BaseCommand):
    """
    Make sure you are already install libsass-python <pip install libsass>
    
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATICFILES_DIRS = [
        "public",
    ]

    INSTALLED_APPS = [
        'custom_commands',
    ]
    
    """
    help = 'Call collectstatic and then sassc'

    def handle(self, *args, **options):
        call_command('collectstatic', verbosity=0, interactive=False)
        csspath = settings.STATIC_ROOT + '/css'
        for file in os.listdir(csspath):
            if file.endswith(".scss"):
                cmd1 = 'sassc ' + os.path.join(csspath, file) + ' > ' + os.path.join(csspath, os.path.splitext(file)[0] + '.css')
                print cmd1
                call(cmd1, shell=True)
        self.stdout.write(self.style.SUCCESS('Successfully'))
        