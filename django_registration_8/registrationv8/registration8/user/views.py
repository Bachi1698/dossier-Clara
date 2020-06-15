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
        if password != re_password :
            message = "mot de pass différent"
            print("1")
        else:
            print("2")
            try:
                validate_email(email)
                isemail = True
                if isemail and not email.isspace() and name is not None and password is not None and re_password is not None:
                    try:
                        try:
                            print("3")
                            exist_user = User.objects.get(username=name)
                        except Exception as e:
                            print("4",e)
                            exist_email = User.objects.get(email=email)
                        message = "l'email ou le username existe déjà"
                    except Exception as e :
                        print("5",e)
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
                        message = " l'enregistrement à bien été effectué"

                    

            except Exception as e:
                message = "l'inscription à échouer"
                print("6",e)
                
    datas = {
            "message":message,
    }
    return render(request,"index.html",datas)