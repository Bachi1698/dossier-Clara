from django.shortcuts import render,redirect
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from . import token as token_
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

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
                            email=email,
                            is_active = False
                        )
                        user.save() 
                        user.password = passe
                        user.set_password(user.password)
                        user.save()
                        current_site = get_current_site(request)
                        subject = 'Activate Your MySite Account'
                        message = render_to_string('account_activation_email.html', {
                            'user': user,
                            'domain': current_site.domain,
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            'token': token_.account_activation_token.make_token(user),
                        })
                        user.email_user(subject, message)
                        message = " merci de vérifier votre email pour la confirmation de votre compte"
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


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and token_.account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('index')
    else:
        return render(request, 'inscription.html')