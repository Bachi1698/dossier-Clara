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

class ProjectAdmin(CustomAddmin):
    list_display = ('titre','types','date_add','date_update','status','image_view')   
    search_fields = ('titre',)    
    ordering = ['titre']    
    fieldsets = [
                  ("info project",{"fields":["titre","types","image"]}),
                  ("standard",{"fields":["status"]})
    ]
    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))

class AppartementAdmin(CustomAddmin):
    list_display = ('lieu','superficie','nombre_douche','date_add','date_update','status','garage','image_view')   
    search_fields = ('lieu',)    
    ordering = ['lieu']    
    fieldsets = [
                  ("info appartement",{"fields":["lieu","superficie","image","nombre_douche","garage","description",]}),
                  ("standard",{"fields":["status"]})
    ]
    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))

def _register(model,admin_class):
    admin.site.register(model,admin_class)

_register(models.Project,ProjectAdmin)
_register(models.Appartement,AppartementAdmin)