from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('',CarPhotoViewSet.as_view({'get': 'list', 'post': 'create'}),name='car_list'),
]