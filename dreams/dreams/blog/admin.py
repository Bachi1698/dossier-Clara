from django.contrib import admin
from . import models 
from django.utils.safestring import mark_safe

# Register your models here.
class CustomAddmin(admin.ModelAdmin):
    actions = ('activate','desactivate')
    list_filter = ('status',)
    list_per_page = 6
    date_hierachy = "date_add"

    def activate(self,request,queryset):
        queryset.update(status=True)
        self.message_user(request,'la selection a été effectué avec succes')
    activate.short_description = "permet d'activer le champs selectionner"

    def desactivate(self,request,queryset):  
        queryset.update(status=False)
        self.message_user(request,'la selection a été effectué avec succes')
    desactivate.short_description = "permet de desactiver le champs selectionner"

class CategorieAdmin(CustomAddmin):
    list_display = ('nom','date_add','date_update','status')   
    search_fields = ('nom',)    
    ordering = ['nom']    
    fieldsets = [
                  ("info categorie",{"fields":["nom"]}),
                  ("standard",{"fields":["status"]})
    ]

class TagAdmin(CustomAddmin):
    list_display = ('nom','date_add','date_update','status')   
    search_fields = ('nom',)    
    ordering = ['nom']    
    fieldsets = [
                  ("info tag",{"fields":["nom"]}),
                  ("standard",{"fields":["status"]})
    ]

class ArticleAdmin(CustomAddmin):
    list_display = ('titre','categorie','date_add','date_update','status','image_view')   
    search_fields = ('titre',)    
    ordering = ['titre']    
    fieldsets = [
                  ("info article",{"fields":["titre","categorie","tag","description","image"]}),
                  ("standard",{"fields":["status"]})
    ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))

class CommentaireAdmin(CustomAddmin):
    list_display = ('user','date_add','date_update','status')   
    search_fields = ('user',)    
    ordering = ['user']    
    fieldsets = [
                  ("info commentaire",{"fields":["user","article"]}),
                  ("standard",{"fields":["status"]})
    ]


def _register(model,admin_class):
    admin.site.register(model,admin_class)

_register(models.Categorie,CategorieAdmin)
_register(models.Tag,TagAdmin)
_register(models.Article,ArticleAdmin)
_register(models.Commentaire,CommentaireAdmin)
