from django.urls import path
from . import views

urlpatterns = [
    path('',views.inscription,name="inscription"),
    path('post',views.is_inscription,name="is_inscription"),

]