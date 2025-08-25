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
                    profile = request.FILES['profile'],
                    usertype = request.POST['usertype'],
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
                request.session['profile']=user.profile.url
                
                if user.usertype == "customer":
                    return redirect('index')
                else:
                    return redirect('bindex')
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
    del request.session['profile']
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
    
def cpass(request):
    user = User.objects.get(email = request.session['email'])
    if request.method == "POST":
        
        if user.password == request.POST['opassword']:
            if request.POST['npassword']==request.POST['cnpassword']:
                user.password = request.POST['npassword']
                user.save()
                return redirect('logout')
            else:
                msg = "New password and confirm password not match"
                if user.usertype == "customer":
                    return render(request,'cpass.html',{'msg':msg})
                else:
                    return render(request,'bcpass.html',{'msg':msg})
        else:
            msg = "Old password not match"
            if user.usertype == "customer":
                return render(request,'cpass.html',{'msg':msg})
            else:
                return render(request,'bcpass.html',{'msg':msg})
                
    else:
        if user.usertype == "customer":
            return render(request,'cpass.html')
        else:
            return render(request,'bcpass.html')
            

def uprofile(request):
    user = User.objects.get(email = request.session['email'])
    if request.method == "POST":
        user.name = request.POST['name']
        user.mobile = request.POST['mobile']
        try:
            user.profile = request.FILES['profile']
            user.save()
            request.session['profile']=user.profile.url
        except:
            pass
        user.save()
        if user.usertype == "customer":
            return redirect('index')
        else:
            return redirect('bindex')
    else:
        if user.usertype == "customer":
            return render(request,'uprofile.html',{'user':user})
        else:
            return render(request,'buprofile.html',{'user':user})
            
    
def bindex(request):
    return render(request,'bindex.html')

def add(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email = request.session['email'])
            Car.objects.create(
                user=user,
                compnaychoice = request.POST['company'],
                cyear = request.POST['cyear'],
                cname = request.POST['cname'],
                cprice = request.POST['cprice'],
                cimage = request.FILES['cimage'],
            )
            msg = "car added succcessfully"
            return render(request,'add.html',{'msg':msg})
        except Exception as e:
            print("=================>",e)
            return redirect('bindex')
    else:
        return render(request,'add.html')
    
def view(request):
    user = User.objects.get(email = request.session['email'])
    car = Car.objects.filter(user=user) 
    print(user)
    return render(request,'view.html',{'car':car})

def cdetails(request,pk):
    user = User.objects.get(email = request.session['email'])
    car = Car.objects.get(pk=pk)
    return render(request,'cdetails.html',{'car':car})

def update(request,pk):
    user = User.objects.get(email = request.session['email'])
    car = Car.objects.get(pk=pk)
    if request.method=="POST":
        car.cname = request.POST["cname"]
        car.cprice = request.POST["cprice"]
        car.cyear = request.POST["cyear"]
        car.compnaychoice == request.POST["company"]
        try:
            car.cimage = request.FILES['cimage']
        except:
            pass
        car.save()
        return redirect('view')
    else:
        return render(request,'update.html',{'car':car})
    
def delete(request, pk):
    user = User.objects.get(email = request.session['email'])
    car = Car.objects.get(pk=pk)
    car.delete()
    
    return redirect('view')