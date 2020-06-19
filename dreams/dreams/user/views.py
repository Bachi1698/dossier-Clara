from django.shortcuts import render
from . import models 
from django.core.validators import validate_email
from django.contrib.auth.models import User
import json
from django.http import JsonResponse 
# Create your views here.
def inscription(request):
    message = ""
    success = False
    
    datas = {

    }
    return render(request,"registration/inscription.html",datas)


def is_inscription(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    re_password = request.POST.get('re_password')
    try:
        if password != re_password:
            print('echec')
            success = False 
            message = " mot de passe différent"
        else:
            print("success")
            try:
                exist_username = User.objects.get(username=username)
                success = False 
                message = "un utilisateur avec le même username existe"
            except Exception as e:
                 
                print(e)   
                user = User(
                    username = username,
                )
                user.save() 

                user.password = password
                user.set_password(user.password)
                user.save()

                success = True 
                message = " utilisateur enragistré"


    except :
        success = False 
        message = " inscription echoué"
        print('inscription echoué')
    data = {
        "success":success,
        "message":message,

    }
    return JsonResponse(data,safe=False)