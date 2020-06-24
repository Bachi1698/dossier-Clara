from django.shortcuts import render,redirect
from . import models 
from django.core.validators import validate_email
from django.contrib.auth.models import User
import json
from django.http import JsonResponse 
from django.contrib.auth import authenticate,login as log,logout
######### email conf
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.core.mail import send_mail

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
    if request.method == 'POST':
        forgotPassword = request.POST.get('forgotPassword')
        print(forgotPassword)        
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
                    is_active = False,
                )
                user.save() 
                print('1')
                user.password = password
                user.set_password(user.password)
                user.save()
                current_site = get_current_site(request) # permet de recuperer le site courant 
                mail_subject = 'Activate your blog account.' # le sujet du mail

                print('2')
                # permet de faire le rendu du mail avec des variable
                message = render_to_string('email/mail_conf.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':account_activation_token.make_token(user),
                })
                # permet d'envoyer le mail il faut signifier dans ke site configuration smpt
                send_mail(
                        mail_subject,
                        message,
                        'marylise@gmail.com',
                        [user.email],
                ) 
                print("3")
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

def activate(request, uidb64, token):
    
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        print(token)
        print(user)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        datas = {
            'confirmation': True,
            'is_actif': True,
            'message': "Votre email a été V"
        }
        return render(request, 'email/email_confirm.html', datas)
    else:
        return render(request, 'email/invalid_link.html')