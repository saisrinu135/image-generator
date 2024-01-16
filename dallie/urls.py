from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('generate-image', generateImage, name='generate-image'),
]