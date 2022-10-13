from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse, request

from django.db.models import Q
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from django.core.files import File

from Customer.models import *
from FashionDesigner.models import *

def index(request):
    return render(request,"index.html")

def fdpage(request):
    return render(request,"fdpage.html")

def fdsignup(request):
    return render(request,"fdsignup.html")

def fdregister(request):
    if request.method=="POST":
        firstname=request.POST['fname'] 
        lastname=request.POST['lname']
        phoneno=request.POST['phoneno'] 
        email=request.POST['email']
        experience=request.POST['experience'] 
        designation=request.POST['designation']
        username=request.POST['uname'] 
        password=request.POST['password']
        flag=Fdsignup.objects.filter(Q(email__iexact=email))
        if flag:
            return redirect("fdsignup")
        else:
            data=Fdsignup(firstname=firstname,lastname=lastname,phoneno=phoneno,email=email,experience=experience,designation=designation,username=username,password=password)
            data.save()
            subject="Thank you for registered"
            email=EmailMessage(subject,"You have Successully registered as designer in Fashion Designer Website",to=[email])  #to will take list of email IDs
            email.send()
            return render(request, "fdsignupsuccess.html")
    else:
        return render(request, "fdsignup.html")

def fdsignin(request):
    return render(request,"fdsignin.html")

def checkfdsignin(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        print(email,password)
        flag=Fdsignup.objects.filter(Q(email__iexact=email) & Q(password__iexact=password))
        if flag:
            request.session['email']=email
            return redirect("fdhome")
        else:
            return render(request,"signupfail.html")
    else:
        return render(request,"fdsignin.html")

def fdhome(request):
    if request.session.get("email",None):
        email=request.session["email"]
        result=Fdsignup.objects.filter(email=email)
        return render(request,"fdhome.html",{"result":result})
    else:
        return redirect(fdsignin)

def fdform(request):
    if request.session.get("email",None):
        email=request.session["email"]
        result=Fdsignup.objects.filter(email=email)
        return render(request,"fdform.html",{"result":result})
    else:
        return redirect(fdsignin)

def fdformstore(request):
    if request.method=="POST" and request.FILES['clothfile']:
        clothname=request.POST['clothname']
        clothfile = request.FILES['clothfile']
        clothgender=request.POST['clothgender']
        clothtype=request.POST['clothtype']
        clothcolour=request.POST['clothcolour']
        clothpattern=request.POST['clothpattern']
        clothsizes=request.POST['clothsizes']
        clothprice=request.POST['clothprice']
        email=request.session["email"]
        username=Fdsignup.objects.filter(email=email).values('username')[0]['username']
        data=Fdform(email=email,username=username,clothname=clothname,clothfile=clothfile,clothgender=clothgender,clothtype=clothtype,
                    clothcolour=clothcolour,clothpattern=clothpattern,clothsizes=clothsizes,clothprice=clothprice)
        data.save()
        return redirect(fdfilesuccess)
    else:
        return redirect(fdform)

def fdfilesuccess(request):
    if request.session.get("email",None):
        return render(request,"fdfilesuccess.html")
    else:
        return redirect(fdsignin)

def fdfiles(request):
    if request.session.get("email",None):
        email=request.session["email"]
        FiResult=Fdform.objects.filter(email=email)
        count=Fdform.objects.filter(email=email).count()
        FdsignupResult=Fdsignup.objects.filter(email=email)
        return render(request, "fdfiles.html",{"FiResult":FiResult,"count":count,'media_url':settings.MEDIA_URL,"FdsignupResult":FdsignupResult})
    else:
        return redirect(fdsignin)

def fdfileview(request,id):
    if request.session.get("email",None):
        result=Fdform.objects.filter(id=id)
        return render(request,"fdfileview.html",{"result":result,'media_url':settings.MEDIA_URL})
    else:
        return redirect(fdsignin)

def fdfiledelete(request,id):
    if request.session.get("email",None):
        Fdform.objects.filter(id=id).delete()
        return redirect(fdfiles)
    else:
        return redirect(fdsignin)

def fdcontactus(request):
    if request.session.get("email",None):
        email=request.session["email"]
        result=Fdsignup.objects.filter(email=email)
        return render(request,"fdcontactus.html",{"result":result})
    else:
        return redirect(fdsignin)

def fdlogout(request):
    if request.session.get("email",None):
        del request.session["email"]
        return redirect(fdpage)
    else:
        return redirect(fdsignin)
        

