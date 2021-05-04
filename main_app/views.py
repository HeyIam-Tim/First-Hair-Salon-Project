# pylint: disable=E1101
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import WomanService, ImageTest
from .serializers import WomanServiceSerializer


class IndexPage(TemplateView):
    template_name = 'main_app/index.html'


class WomenPage(TemplateView):
    template_name = 'main_app/women.html'


class WomenPageAPI(APIView):
    def get(self, request, format=None):
        women_services = WomanService.objects.all()
        serializer = WomanServiceSerializer(women_services, many=True)
        return Response(serializer.data)


class MenPage(TemplateView):
    template_name = 'main_app/men.html'


class KidsPage(TemplateView):
    template_name = 'main_app/kids.html'



class ImageTestView(ListView):
    model = ImageTest
    template_name = 'main_app/image.html'
    context_object_name = 'images'
    