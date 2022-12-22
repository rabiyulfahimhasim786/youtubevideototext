from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.file_upload, name='file_upload'),
    path('data/', views.audio_conversion, name='audio_conversion'),
    path('homepage/', views.id_upload, name='id_upload'),
    path('datapage/', views.sub_transcript, name='sub_transcript'),
]