from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings


# set the default Django settings modules for the 'celery proejct'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryPractice.settings')

app = Celery('celeryPractice')

# using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace = "CELERY" means all celery related configuration key
# should have a 'CELERY' prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# load task modules from all registered Django app configs
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))