from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class MainView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
    login_url = '/login'
    