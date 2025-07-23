from django.shortcuts import render,redirect
from .models import *
from django.core.mail import send_mail
from django.conf import settings
import random

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

def fpass(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email = request.POST['email'])
            otp = random.randint(1001,9999)
            subject = 'OTP for forget Password'
            message = 'Hi'+user.name+'your otp is :' + str(otp)
            email_form = settings.EMAIL_HOST_USER
            recipient_list = [user.email,]
            send_mail(subject,message,email_form,recipient_list)
            request.session['email'] = user.email
            request.session['otp'] = otp
            return render(request,'otp.html')
            
        except:
            msg = "Email does not exist"
            return render(request,'fpass.html',{'msg':msg})
    else:
        return render(request,'fpass.html')

def otp(request):
    if request.method == "POST":
        try:
            otp = int(request.session['otp'])
            uotp = int(request.POST['uotp'])
            if otp == uotp:
                del request.session['otp']
                return render(request,'newpass.html')
            else:
                msg = "invalid otp"
                return render(request,'otp.html',{'msg':msg})
        except:
            pass
    else:
        return render(request,'otp.html')

def newpass(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.session['email'])
            if request.POST['npassword']==request.POST['cnpassword']:
                user.password = request.POST['npassword']
                user.save()
                del request.session['email']
                return redirect('login')
            else:
                msg = "new password and confirm new password not match"
                return render(request,'newpass.html',{'msg':msg})
        except:
            pass
    else:
        return render(request,'newpass.html')