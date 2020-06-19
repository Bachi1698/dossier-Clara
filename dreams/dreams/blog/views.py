from django.shortcuts import render
from . import models 
from website import models as models_website

# Create your views here.
def blog(request):
    article = models.Article.objects.filter(status=True)
    categorie = models.Categorie.objects.filter(status=True)
    article_r = models.Article.objects.filter(status=True).order_by('date_add')[:4]
    site_info = models_website.SiteInfo.objects.filter(status=True)[:1].get()
    tag = models.Tag.objects.filter(status=True)
    datas = {
            "article":article,
            "categorie":categorie,
            "article_r":article_r,
            "tag":tag,
            "site_info":site_info,
    }
    return render(request,"pages/blog.html",datas)

def blog_single(request,slug):
    article = models.Article.objects.get(slug=slug)
    categorie = models.Categorie.objects.filter(status=True)
    article_r = models.Article.objects.filter(status=True).order_by('date_add')[:4]
    tag = models.Tag.objects.filter(status=True)
    site_info = models_website.SiteInfo.objects.filter(status=True)[:1].get()
    datas = {
            "article":article,
            "site_info":site_info,
            "categorie":categorie,
            "article_r":article_r,
            "tag":tag,
    }
    return render(request,'pages/single-blog.html',datas)