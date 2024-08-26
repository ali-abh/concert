from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
import ticketsale
from django.conf import settings
import ticketsale.views
# Create your views here.
def loginView(request):            
    if request.method=='POST':
        username=request.POST.get('username') 
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
   
    if user is not None:
        login(request,user)
        if request.GET.get('next'):
            return HttpResponseRedirect(request.GET.get('next'))
        
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

    else:
        context ={
            "username":username,
            "کاربری با این مشحصات یافت نشد":"erroMessage"
        }
        return render(request, "accounts/login.html",{})

