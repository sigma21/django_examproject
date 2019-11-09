from django.shortcuts import render, redirect
from django.contrib import messages, auth

from accounts.models import Account


def dashboard(request):
    return render(request, 'dashboard.html')


def register(request):
    if request.method == "POST":
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        dob = request.POST['dateofbirth']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        # check if passwords match
        if password == password2:
            # check email
            if Account.objects.filter(email=email).exists():
                # messages.error(request, "That email is already registered.")
                print("bu mail kullanılıyor")
                return redirect("register")
            else:
                user = Account.objects.create_user(email=email, password=password,
                first_name=first_name, last_name=last_name, dob=dob)
                
                # Login after registration
                user.save()
                auth.login(request, user)
                # messages.success(request, "You are now logged in")
                print("kayıt başarılı")
                return redirect("dashboard")
                
                # register then redirect to login page
                # user.save()
                # messages.success(request, "You are now registered")
                # return redirect("homepage")
        else:
            # messages.error(request, "Passwords do not match!")
            print("şifreler aynı değil")
            return redirect("register")

    else:
        return render(request, "register.html")



def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            # messages.success(request, "You are successfully logged in.")
            print("login başarılı")
            return redirect('dashboard')
        else:
            # messages.error(request, "Invalid credentials")
            print("login hatalı")
            return redirect('login')

    else:
        print("not post method!")
        return render(request, "login.html")

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        # messages.success(request, "You are now logged out.")
        print("logout gerçekleştirildi")
        return redirect("homepage")
