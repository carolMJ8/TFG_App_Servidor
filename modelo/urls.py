from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    #path('', include(router.urls))
    path('', views.index, name='index'),
]