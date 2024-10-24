from . import views
from django.urls import path

app_name = "ARWeb"

urlpatterns = [
    path("home/tr", views.indexTr, name="indexTr"),
    path("home/en", views.indexEn, name="indexEn"),
    path("ourMission/tr", views.ourMissionTr, name="ourMissionTr"),
    path("ourMission/en", views.ourMissionEn, name="ourMissionEn"),
    path("ourVision/tr", views.ourVisionTr, name="ourVisionTr"),
    path("ourVision/en", views.ourVisionEn, name="ourVisionEn"),
    path("about/tr", views.aboutTr, name="aboutTr"),
    path("about/en", views.aboutEn, name="aboutEn"),
    path("communication/tr", views.communicationTr, name="communicationTr"),
    path("communication/en", views.communicationEn, name="communicationEn"),
    path("error/", views.error, name="error"),
]
