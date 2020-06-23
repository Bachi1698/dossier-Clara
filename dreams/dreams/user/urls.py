from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('register',views.register,name='register'),
    path('forgot',views.forgot,name='forgot'),
    path('post',views.is_inscription,name="is_inscription"),
    path('is_login',views.is_login,name='is_login'),
    path('is_logout',views.is_logout,name="is_logout")

]