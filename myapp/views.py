from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def pricing(request):
    return render(request,'pricing.html')

def cars(request):
    return render(request,'car.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def singup(request):
    if request.method=="POST":
        try:
            user = User.objects.get(email=request.POST['email'])
            if user:
                msg = "Email already Exists"
                return render(request, 'singup.html', {'msg': msg})
        except:
            if request.POST['password'] == request.POST['cpassword']:
                User.objects.create(
                    name = request.POST['name'],
                    email = request.POST['email'],
                    mobile = request.POST['mobile'],
                    password = request.POST['password'],
                )
                msg = "signup successfully !!!"
                return render(request,'login.html',{'msg':msg})
            else:
                msg = "password and confirm password does't match !!!"
                return render(request,'singup.html',{'msg':msg})
    else:
        return render(request,'singup.html')

def login(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.POST['email'])
            if user.password==request.POST['password']:
                request.session['email']=user.email
                return redirect('index')
            else:
                msg = "password doest not macth"
                return render(request, 'login.html',{'msg':msg})
        except:
            msg = "email does not exists"
            return render(request, 'login.html',{'msg':msg})
    
    else:
        return render(request, 'login.html')

def logout(request):
    del request.session['email']
    return redirect('login')