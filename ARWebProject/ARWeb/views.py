import os
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from firebase_admin import db
from datetime import datetime
from django.shortcuts import redirect, render
from django.contrib import messages


def loginTr(request):
    if "user_id" in request.session:
        return HttpResponseRedirect("http://127.0.0.1:8000/home/tr")

    if request.method == "POST":
        mail = request.POST.get("email")
        sifre = request.POST.get("sifre")

        ref = db.reference("users")
        data = ref.get()

        if data:
            for key, value in data.items():
                if value["mail"] == mail and value["password"] == sifre:
                    request.session["user_id"] = key
                    return HttpResponseRedirect("http://127.0.0.1:8000/home/tr")

        messages.error(request, "Geçersiz mail veya şifre.")

    return render(request, "../templates/ARWebProject/loginTr.html")


def loginEn(request):
    if "user_id" in request.session:
        return HttpResponseRedirect("http://127.0.0.1:8000/home/en")

    if request.method == "POST":
        mail = request.POST.get("email")
        password = request.POST.get("password")

        ref = db.reference("users")
        data = ref.get()

        if data:
            for key, value in data.items():
                if value["mail"] == mail and value["password"] == password:
                    request.session["user_id"] = key
                    return HttpResponseRedirect("http://127.0.0.1:8000/home/en")

        messages.error(request, "Invalid email or password.")

    return render(request, "../templates/ARWebProject/loginEn.html")


def logout(request):
    request.session.flush()
    previous_page = request.META.get("HTTP_REFERER", "/")
    return redirect(previous_page)


def faqTr(request):
    return render(request, "../templates/ARWebProject/faqTr.html")


def faqEn(request):
    return render(request, "../templates/ARWebProject/faqEn.html")


def termsOfUseTr(request):
    return render(request, "../templates/ARWebProject/termsOfUseTr.html")


def termsOfUseEn(request):
    return render(request, "../templates/ARWebProject/termsOfUseEn.html")


def download(request, lang, device):
    if "user_id" not in request.session:
        return redirect("/register/" + lang)
    else:
        file_path = ""
        if device == "android":
            file_path = "ARWeb/static/ARWebProject/APKFiles/android.apk"
        elif device == "ios":
            file_path = "ARWeb/static/ARWebProject/APKFiles/android.apk"

        # Dosyanın varlığını kontrol et ve dosyayı indir
        if os.path.exists(file_path):
            with open(file_path, "rb") as file:
                response = HttpResponse(
                    file.read(), content_type="application/octet-stream"
                )
                file_name = "Dede Korkut.apk"
                response["Content-Disposition"] = f'attachment; filename="{file_name}"'
                return response
        else:
            # Dosya bulunamazsa anasayfaya yönlendir
            if lang == "tr":
                return redirect("/home/" + lang)
            else:
                return redirect("/home/" + lang)


def check_date_format(date_string):
    try:
        datetime.strptime(date_string, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def registerTr(request):
    if request.method == "POST":
        isim = request.POST.get("isim")
        soyisim = request.POST.get("soyisim")
        dogumTarihi = request.POST.get("dogumTarihi")
        mail = request.POST.get("email")
        sifre = request.POST.get("sifre")
        sifreDogrulama = request.POST.get("sifreDogrulama")
        if check_date_format(dogumTarihi):
            if sifre == sifreDogrulama:
                try:
                    ref = db.reference("users")
                    ref.push(
                        {
                            "name": isim,
                            "surname": soyisim,
                            "dateOfBirth": dogumTarihi,
                            "mail": mail,
                            "password": sifre,
                        }
                    )

                    return HttpResponseRedirect("http://127.0.0.1:8000/login/tr")
                except Exception as e:
                    pass
            else:
                messages.error(request, "Şifre ve doğrulama şifresi aynı olmalıdır.")
        else:
            messages.error(request, "Doğum tarihinizi GG/AA/YYYY olacak şekilde girin.")

    return render(request, "../templates/ARWebProject/registerTr.html")


def registerEn(request):
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        dateOfBirth = request.POST.get("dateOfBirth")
        mail = request.POST.get("email")
        password = request.POST.get("password")
        passwordConfirm = request.POST.get("passwordConfirm")
        if check_date_format(dateOfBirth):
            if password == passwordConfirm:
                try:
                    ref = db.reference("users")
                    ref.push(
                        {
                            "name": name,
                            "surname": surname,
                            "dateOfBirth": dateOfBirth,
                            "mail": mail,
                            "password": password,
                        }
                    )

                    return HttpResponseRedirect("http://127.0.0.1:8000/login/en")
                except Exception as e:
                    pass
            else:
                messages.error(
                    request, "Password and verification password must be the same."
                )
        else:
            messages.error(request, "Enter your date of birth as DD/MM/YYYY.")

    return render(request, "../templates/ARWebProject/registerEn.html")


def indexTr(request):
    if "user_id" in request.session:
        context = {"session_active": True}
    else:
        context = {"session_active": False}

    return render(request, "../templates/ARWebProject/indexTr.html", context)


def indexEn(request):
    if "user_id" in request.session:
        context = {"session_active": True}
    else:
        context = {"session_active": False}

    return render(request, "../templates/ARWebProject/indexEn.html", context)


def ourMissionTr(request):
    if "user_id" in request.session:
        context = {"session_active": True}
    else:
        context = {"session_active": False}

    return render(request, "../templates/ARWebProject/ourMissionTr.html", context)


def ourMissionEn(request):
    if "user_id" in request.session:
        context = {"session_active": True}
    else:
        context = {"session_active": False}

    return render(request, "../templates/ARWebProject/ourMissionEn.html", context)


def ourVisionTr(request):
    if "user_id" in request.session:
        context = {"session_active": True}
    else:
        context = {"session_active": False}

    return render(request, "../templates/ARWebProject/ourVisionTr.html", context)


def ourVisionEn(request):
    if "user_id" in request.session:
        context = {"session_active": True}
    else:
        context = {"session_active": False}

    return render(request, "../templates/ARWebProject/ourVisionEn.html", context)


def aboutTr(request):
    if "user_id" in request.session:
        context = {"session_active": True}
    else:
        context = {"session_active": False}

    return render(request, "../templates/ARWebProject/aboutTr.html", context)


def aboutEn(request):
    if "user_id" in request.session:
        context = {"session_active": True}
    else:
        context = {"session_active": False}

    return render(request, "../templates/ARWebProject/aboutEn.html", context)


def communicationTr(request):
    if "user_id" in request.session:
        context = {"session_active": True}
    else:
        context = {"session_active": False}

    return render(request, "../templates/ARWebProject/communicationTr.html", context)


def communicationEn(request):
    if "user_id" in request.session:
        context = {"session_active": True}
    else:
        context = {"session_active": False}

    return render(request, "../templates/ARWebProject/communicationEn.html", context)


def error(request):
    return render(request, "../templates/ARWebProject/error.html")
