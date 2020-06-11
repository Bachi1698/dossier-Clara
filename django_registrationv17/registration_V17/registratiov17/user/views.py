from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def inscription(request):
    message = ""
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        username = request.POST.get('name')
        email = request.POST.get('email')
        genre = request.POST.get('genre')
        passe = request.POST.get('pass')
        repass = request.POST.get('repass')
        validate_email(email)
        isemail = True
        if passe != repass:
            message = "mot de passe incorrect "
            print("mot de passe incorrect")
        else:
            message = "correct"
            print("success")

            if isemail and not email.isspace() and first_name is not None and not first_name.isspace() and last_name is not None and passe is not None and repass is not None:
                user = User(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email
                )
                user.save()
                user.password = passe
                user.set_password(user.password)
                user.save()
                message = " l'enregistrement a été effectué avec succes"
                try:
                    us = authenticate(username=username, password=passe)
                    if us.is_active:
                        login(request,us)
                        return redirect('index')
                except:
                    pass
            
            else:
                message = "l'inscription a échoué"
                print("inscription echoué")


    datas = {
            "message":message,
    }
    return render(request,"inscription.html",datas)

def is_login(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        password = request.POST.get("pass")
        user = authenticate(username=name,password=password)
        if user is not None and user.is_active:
            login(request,user)
            return redirect('index')
        else:
            print("login échoué")

    datas = {

    }
    return render(request,"login.html",datas)

def index(request):
    datas = {

    }
    return render(request,"index.html",datas)

def is_deconnexion(request):
    logout(request)
    return redirect('login')