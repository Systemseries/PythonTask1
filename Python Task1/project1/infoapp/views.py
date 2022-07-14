from django.shortcuts import render,HttpResponseRedirect
from .models import clientinfo,user2
from .forms import clientform,userform,signupform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def base(request):
    return render(request,'base.html')

def index(request):
    if request.method=="POST":
       fm=clientform(request.POST,request.FILES)
       if fm.is_valid():
            fm.save()
    else:
       fm=clientform()
    return render(request,'index.html',{'fm':fm})

def info(request):
    pi=clientinfo.objects.all()
    return render(request,'info.html',{'pi':pi})

def index2(request):
    if request.method=="POST":
       fm=userform(request.POST,request.FILES)
       if fm.is_valid():
            fm.save()
    else:
       fm=userform()
    return render(request,'userindex.html',{'fm':fm})

def info1(request):
 pi=user2.objects.all()
 return render(request,'info2.html',{'pi':pi})

def delete(request,id):
    if request.method=="POST":
        ki=clientinfo.objects.get(pk=id)
        ki.delete()
    return HttpResponseRedirect('/info/') 

def update(request,id):
    if request.method=="POST":
        ki=clientinfo.objects.get(pk=id)
        fm=clientform(request.POST,instance=ki)
        if fm.is_valid():
            fm.save()
    else:
        ki=clientinfo.objects.get(pk=id)
        fm=clientform(instance=ki)
    return render(request,'update.html',{'fm':fm})  
    

def signup(request):
    if request.method=="POST":
        fm=signupform(request.POST)
        if fm.is_valid():
            messages.success(request, 'congratulations become admin')
            fm.save()
    else:
        fm=signupform()
    return render(request,'register.html',{'fm':fm})

def user_login(request):
    if request.method=="POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/info/')
    else:
        fm=AuthenticationForm()
    return render(request,'login.html',{'fm':fm})

def logout1(request):
    logout(request)
    return HttpResponseRedirect('/login/')         




