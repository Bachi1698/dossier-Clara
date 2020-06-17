from django.shortcuts import render

# Create your views here.
def appartement(request):
    datas = {

    }
    return render(request,"pages/Apartment.html",datas)

def project(request):
    datas = {

    }
    return render(request,"pages/project.html",datas)
