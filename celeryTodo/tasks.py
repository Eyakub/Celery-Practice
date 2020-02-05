from __future__ import absolute_import, unicode_literals
from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
import string
from django.contrib.auth.models import User


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def count_widgets():
    return Widget.objects.count()


@shared_task
def rename_widget(widget_id, name):
    w = Widget.objects.get(id=widget_id)
    w.name = name
    w.save()


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_email_task():
    sleep(10)
    send_mail('Celery Task worked',
        'This is proof the task worked',
        'eyakubsorkar@gmail.com',
        ['doxeb@247web.net']
    )
    return None


@shared_task
def create_random_user_accounts(total):
    print('inside create random user')
    for i in range(total):
        username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        email = '{}@example.com'.format(username)
        password = get_random_string(10)
        User.objects.create_user(username=username, email=email, password=password)
        print('user created ', i)
    return '{} random users created with success!'.format(total)
