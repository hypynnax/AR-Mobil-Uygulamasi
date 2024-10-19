from django.shortcuts import render


def indexTr(request):
    return render(request, "../templates/ARWebProject/indexTr.html")


def indexEn(request):
    return render(request, "../templates/ARWebProject/indexEn.html")
