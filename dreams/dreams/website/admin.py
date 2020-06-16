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

class AboutAdmin(CustomAddmin):
    list_display = ('nom','image_view','date_add','date_update','status')   
    search_fields = ('nom',)    
    ordering = ['nom']    
    fieldsets = [
                  ("info about",{"fields":["nom","image"]}),
                  ("standard",{"fields":["status"]})
    ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))

class ContactAdmin(CustomAddmin):
    list_display = ('name','email','subject','date_add','date_update','status')   
    search_fields = ('name',)    
    ordering = ['name']    
    fieldsets = [
                  ("info contact",{"fields":["name","email","subject"]}),
                  ("standard",{"fields":["status"]})
    ]

class SiteInfoAdmin(CustomAddmin):
    list_display = ('telephone','email','slogan','mapping','date_add','date_update','status','logo_view')   
    search_fields = ('email',)    
    ordering = ['email']    
    fieldsets = [
                  ("info site info",{"fields":["email","telephone","slogan","logo","mapping"]}),
                  ("standard",{"fields":["status"]})
    ]
    def logo_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.logo.url))

class SocialCountAdmin(CustomAddmin):
    list_display = ('reseau','lien','date_add','date_update','status',)   
    search_fields = ('reseau',)    
    ordering = ['reseau']    
    fieldsets = [
                  ("info réseaux sociaux",{"fields":["reseau","lien","icones"]}),
                  ("standard",{"fields":["status"]})
    ]

def _register(model,admin_class):
    admin.site.register(model,admin_class)

_register(models.About,AboutAdmin)
_register(models.Contact,ContactAdmin)
_register(models.SiteInfo,SiteInfoAdmin)
_register(models.SocialCount,SocialCountAdmin)



