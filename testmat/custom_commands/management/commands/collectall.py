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
        
        
        csspath = os.path.join(settings.STATIC_ROOT, 'css')
        sasspath = os.path.join(settings.STATIC_ROOT, 'sass')
        #csspath = settings.STATIC_ROOT + '/css'
        for file in os.listdir(sasspath):
            if file.endswith(".scss"):
                cmd1 = 'sassc ' + os.path.join(sasspath, file) + ' > ' + os.path.join(csspath, os.path.splitext(file)[0] + '.css')
                print cmd1
                call(cmd1, shell=True)
                os.remove(os.path.join(sasspath, file))
        os.rmdir(sasspath)
        self.stdout.write(self.style.SUCCESS('Successfully'))
        