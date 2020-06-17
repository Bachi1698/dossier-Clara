from django.urls import path
from . import views

urlpatterns = [
    path('',views.appartement,name="appartement"),
    path('project',views.project,name="project")

]