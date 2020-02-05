from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.http import HttpResponse
from . import tasks
from django.views.generic.list import ListView

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
        print('total->', total)
        create_random_user_accounts(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('users_list')
