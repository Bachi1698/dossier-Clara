from django.shortcuts import render
from django.core.validators import validate_email
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    message = ""
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        if password != re_password:
            message = "mot de passe différent"
            print("1")
        else:           
            print("2")                
            try:
                validate_email(email)
                isemail = True
                if isemail and not email.isspace() and not name.isspace() and name is not None and password is not None and re_password is not None:
                    try:
                        try:
                            exist_username = User.objects.get(username=name)
                        except Exception as e:
                            print("3",e)
                            exist_email = User.objects.get(email=email)
                        message = "l'email ou l'username son déjà utilisé"
                    except Exception as e:
                        print('4',e)
                        user = User(
                            username = name,
                            email = email,
                            first_name = name,
                            last_name = name,
                        )
                        user.save()
                        user.password = password
                        user.set_password(user.password)
                        user.save()
                        message = "l'inscription a été effectué avec success"
                        
            except Exception as e:
                print("5",e)
                message = "l'inscription à échouer"

    datas = {
            "message":message,
    }
    return render(request,"index.html",datas)