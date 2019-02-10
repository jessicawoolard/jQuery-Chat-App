from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, View
from .models import Message


class HomeView(TemplateView):
    template_name = 'chat/index.html'


class ChatIndex(View):
    pass
