# pylint: disable=E1101
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import MensService


class IndexPage(TemplateView):
    template_name = 'main_app/index.html'


class WomenPage(TemplateView):
    template_name = 'main_app/women.html'


class KidsPage(TemplateView):
    template_name = 'main_app/kids.html'



