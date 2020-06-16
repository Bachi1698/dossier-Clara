from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('inscription',views.inscription,name="inscription"),
    path('login',views.is_login,name="login"),
    path('deconnexion',views.is_deconnexion,name="deconnexion"),
    path('activate/<uidb64>[0-9A-Za-z_\-]/<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}', views.activate, name='activate'),

]
