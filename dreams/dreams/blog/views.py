from django.shortcuts import render
from . import models 

# Create your views here.
def blog(request):
    article = models.Article.objects.filter(status=True)
    categorie = models.Categorie.objects.filter(status=True)
    article_r = models.Article.objects.filter(status=True).order_by('date_add')[:4]
    tag = models.Tag.objects.filter(status=True)
    datas = {
            "article":article,
            "categorie":categorie,
            "article_r":article_r,
            "tag":tag,
    }
    return render(request,"pages/blog.html",datas)

def blog_single(request):
    datas = {

    }
    return render(request,'pages/single-blog.html',datas)