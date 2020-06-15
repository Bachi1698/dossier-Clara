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
        
        if passe != repass:
            message = "mot de passe incorrect "
            print("mot de passe incorrect")
        else:
            message = "correct"
            print("success")
            try:
                print("3")
                validate_email(email)
                isemail = True
                if  isemail and not email.isspace() and first_name is not None and not first_name.isspace() and last_name is not None and passe is not None and repass is not None:
                    try:
                        print("2")
                        try:
                            exist_user = User.objects.get(username=username)
                        except :
                            exist_user = User.objects.get(email=email)

                        message = "un utilisateur avec le même username ..."
                    except Exception as e :
                        print("1", e)
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
                        except Exception as e:
                             print("4", e)
            
                
            except Exception as e:
                print("5", e)
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