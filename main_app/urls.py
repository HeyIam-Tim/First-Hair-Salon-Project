from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('women/', views.WomenPage.as_view(), name='women'),
    path('men/', views.MenPage.as_view(), name='men'),
    path('kids/', views.KidsPage.as_view(), name='kids'),
]


