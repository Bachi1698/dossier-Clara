from django.shortcuts import render
from django.core.validators import validate_email
from django.contrib.auth.models import User
from . import models
from dreamsApp import models as models_dreamsApp
# Create your views here.
def home(request):
    about = models.About.objects.filter(status=True)[:1]
    types = models_dreamsApp.Type.objects.filter(status=True)
    site_info = models.SiteInfo.objects.filter(status=True)[:1].get()
    project = models_dreamsApp.Project.objects.filter(status=True)
    datas = {
            "about":about, 
            "site_info":site_info, 
            "project":project,   
            "types":types,      
    }
    return render(request,"pages/index.html",datas)

def contact(request):
    site_info = models.SiteInfo.objects.filter(status=True)[:1].get()
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
                "site_info":site_info, 
    }
    return render(request,"pages/contact.html",datas)


def about(request):
    about = models.About.objects.filter(status=True)[:1]
    site_info = models.SiteInfo.objects.filter(status=True)[:1].get()
    datas = {
           "about":about, 
           "site_info":site_info,
    }
    return render(request,"pages/about.html",datas)

def service(request):
    site_info = models.SiteInfo.objects.filter(status=True)[:1].get()
    service = models.Service.objects.filter(status=True)
    datas = {
            "site_info":site_info,
            "service":service,
    }
    return render(request,"pages/services.html",datas)
