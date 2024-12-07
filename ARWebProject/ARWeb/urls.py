from . import views
from django.urls import path

app_name = "ARWeb"

urlpatterns = [
    path("login/tr", views.loginTr, name="loginTr"),
    path("login/en", views.loginEn, name="loginEn"),
    path("register/tr", views.registerTr, name="registerTr"),
    path("register/en", views.registerEn, name="registerEn"),
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
    path("faq/tr", views.faqTr, name="faqTr"),
    path("faq/en", views.faqEn, name="faqEn"),
    path("termsOfUse/tr", views.termsOfUseTr, name="termsOfUseTr"),
    path("termsOfUse/en", views.termsOfUseEn, name="termsOfUseEn"),
    path("logout/", views.logout, name="logout"),
    path("download/<str:lang>/<str:device>", views.download, name="download"),
    path("error/", views.error, name="error"),
]
