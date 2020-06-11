from django.shortcuts import render

# Create your views here.
def blog(request):
    datas = {

    }
    return render(request,'blog-single.html',datas)