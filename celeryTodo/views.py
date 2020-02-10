from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.http import HttpResponse
from . import tasks
from django.views.generic.list import ListView
from django.core.mail import send_mail

from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts


def index(request):
    tasks.send_email_task()
    return HttpResponse('<h1>Done</h1>')


class UsersListView(ListView):
    template_name = 'users_list.html'
    model = User


class GenerateRandomUserView(FormView):
    template_name = 'generate_random_users.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        print('inside form validation')
        total = form.cleaned_data.get('total')

        """
        instead of calling the create_random_user_account we've
        called with .delay(), this way we are instructing celery
        to execute this function in the background
        then django keep processing my view GenerateRandomUserView
        """
        create_random_user_accounts.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('users_list')


class SendMailView(View):
    def send_mail_celery(self):
        send_mail(
            'Celery test',
            'Celery schedule tasking',
            'eyakubsorkar@gmail.com',
            ['eyakub.tryonyx@gmail.com',],
            fail_silently=False,
        )