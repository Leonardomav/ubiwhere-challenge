import django
import pydoc
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'ubiwhere.settings'
django.setup()
pydoc.cli()
