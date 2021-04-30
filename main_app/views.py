from django.shortcuts import render
from django.views.generic import TemplateView


class IndexPage(TemplateView):
    template_name = 'main_app/index.html'


class WomenPage(TemplateView):
    template_name = 'main_app/women.html'


class MenPage(TemplateView):
    template_name = 'main_app/men.html'


class KidsPage(TemplateView):
    template_name = 'main_app/kids.html'



