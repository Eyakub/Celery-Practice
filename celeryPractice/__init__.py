from __future__ import absolute_import, unicode_literals


# this will make sure the app is always imported when
# django starts so that shred_task will use this app
from .celery import app as celery_app


__all__ = ('celery_app')
