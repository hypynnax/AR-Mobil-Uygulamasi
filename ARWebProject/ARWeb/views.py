from django.shortcuts import render


def indexTr(request):
    return render(request, "../templates/ARWebProject/indexTr.html")


def indexEn(request):
    return render(request, "../templates/ARWebProject/indexEn.html")


def ourMissionTr(request):
    return render(request, "../templates/ARWebProject/ourMissionTr.html")


def ourMissionEn(request):
    return render(request, "../templates/ARWebProject/ourMissionEn.html")


def ourVisionTr(request):
    return render(request, "../templates/ARWebProject/ourVisionTr.html")


def ourVisionEn(request):
    return render(request, "../templates/ARWebProject/ourVisionEn.html")


def aboutTr(request):
    return render(request, "../templates/ARWebProject/aboutTr.html")


def aboutEn(request):
    return render(request, "../templates/ARWebProject/aboutEn.html")


def communicationTr(request):
    return render(request, "../templates/ARWebProject/communicationTr.html")


def communicationEn(request):
    return render(request, "../templates/ARWebProject/communicationEn.html")


def error(request):
    return render(request, "../templates/ARWebProject/error.html")
