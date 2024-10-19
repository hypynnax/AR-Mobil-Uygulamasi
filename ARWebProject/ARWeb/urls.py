from . import views
from django.urls import path

app_name = 'ARWeb'

urlpatterns = [
    path('home/tr', views.indexTr, name='indexTr'),
    path('home/en', views.indexEn, name='indexEn'),
]