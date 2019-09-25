from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.shortcuts import render
from django.http import HttpResponse
from . import tasks


def index(request):
    tasks.send_email_task()
    return HttpResponse('<h1>Done</h1>')

