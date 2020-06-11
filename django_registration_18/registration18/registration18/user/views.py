from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    # User
    user = User(username =username, first_name = first_name, last_name = last_name, email = email)
    user.save()
    
    # Profile
    
    user.profile.contacts = contacts
    user.profile.image = img
    user.profile.birth_date = birth_date
    user.profile.genre = genre

    user.save()
    
    # Password
    
    user.password = password
    user.set_password(user.password)
    user.save()
    datas = {

    }
    return render(request,"index.html",datas)