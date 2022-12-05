from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.file_upload, name='file_upload'),
    path('data/', views.audio_conversion, name='audio_conversion'),
]