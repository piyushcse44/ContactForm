from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate

# Create your views here.

def home(request):
    return render(request,'user/home.html')

def Login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        

        try:          
            user =  User.objects.get(username=username)
            name = user.first_name
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                msg = 'Username or Passwor is incorrect'
                return render(request,'user/login_page.html',{'msg':msg})   
        except:
            msg = 'Username or Passwor is incorrect'
            return render(request,'user/login_page.html',{'msg':msg})


    return render(request,'user/login_page.html')        


def logout_user(request):
    logout(request)
    return redirect('/')   




      





            
        

    

