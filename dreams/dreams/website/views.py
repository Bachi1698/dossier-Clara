from django.shortcuts import render
from django.core.validators import validate_email
from django.contrib.auth.models import User
from . import models
# Create your views here.
def home(request):
    datas = {

    }
    return render(request,"pages/index.html",datas)

def contact(request):
    message = ""
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        try:
            validate_email(email)
            isemail = True
            if isemail and not email.isspace() and email is not None and name is not None and message is not None:
                print("1")
                contact = models.Contact(
                    name = name,
                    email = email,
                    subject = subject,
                    message = message

                )
                contact.save()
                print("3")
                message = "l'enregistrement a bien été effectué"
        except :
            message = "email incorrect"
            print("2")

        
    datas = {
                "message":message,
    }
    return render(request,"pages/contact.html",datas)


def about(request):
    datas = {

    }
    return render(request,"pages/about.html",datas)