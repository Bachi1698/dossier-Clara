from django.shortcuts import render

# Create your views here.
def blog(request):
    datas = {

    }
    return render(request,"pages/blog.html",datas)

def blog_single(request):
    datas = {

    }
    return render(request,'pages/single-blog.html',datas)