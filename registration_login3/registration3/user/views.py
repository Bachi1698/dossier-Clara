from django.shortcuts import render,redirect
from . import models 
from django.core.validators import validate_email
from django.contrib.auth.models import User
import json
from django.http import JsonResponse 
from django.contrib.auth import authenticate,login as log,logout

# Create your views here.
def index(request):
    datas = {

    }
    return render(request,"index.html",datas)

def login(request):
    datas = {

    }
    return render(request,"login-16.html",datas)

def register(request):
    datas = {

    }
    return render(request,"register-16.html",datas)

def forgot(request):
    datas = {

    }
    return render(request,"forgot-password-16.html",datas)

def is_inscription(request):
        ### recupération des données
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    re_password = request.POST.get('re_password')
    try:
        if password != re_password:
            print('echec')
            success = False 
            message = " mot de passe différent"
        else:
            print("success")
            try:
                try:
                    exist_username = User.objects.get(username=username)
                    success = False 
                    print("4")
                    message = "un utilisateur avec le même username existe"
                except:
                    exist_email = User.objects.get(email=email)
                    print("1")
                    success = False 
                    message = "un utilisateur avec le même mail existe"
            except Exception as e:
                 
                print(e)   
                user = User(
                    username = username,
                    email = email,
                )
                user.save() 

                user.password = password
                user.set_password(user.password)
                user.save()

                success = True 
                message = " utilisateur enregistré"


    except :
        success = False 
        message = " inscription echoué"
        print('inscription echoué')

    data = {
        "success":success,
        "message":message,

    }
    return JsonResponse(data,safe=False)
    
def is_login(request):
    password = request.POST.get('password')
    username = request.POST.get('username')
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        log(request,user)
        message = "bienvenue"
        success = True
    else:
        print("login echoué")
        message = "veuillez vérifier vos informations"
        success = False
    data = {
        'message':message,
        'success':success,
    }
    return JsonResponse(data,safe=False)

def is_logout(request):
    logout(request)
    return redirect('login')