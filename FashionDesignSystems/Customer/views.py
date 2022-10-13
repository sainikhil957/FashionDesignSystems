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


def cupage(request):
    return render(request,"cupage.html")

def cusignup(request):
    return render(request,"cusignup.html")

def curegister(request):
    if request.method=="POST":
        firstname=request.POST['fname'] 
        lastname=request.POST['lname']
        dateofbirth=request.POST['dateofbirth']
        phoneno=request.POST['phoneno']
        email=request.POST['email']
        address=request.POST['address']
        username=request.POST['uname'] 
        password=request.POST['password']
        data=Cusignup(firstname=firstname,lastname=lastname,dateofbirth=dateofbirth,phoneno=phoneno,
                        email=email,address=address,username=username,password=password)
        data.save()
        subject="Thank you dear customer for registered"
        email=EmailMessage(subject,"You have Successully registered as customer in Fashion Designer Website",to=[email])
        email.send()
        return render(request, "cusignupsuccess.html")
    else:
        return render(request, "cusignup.html")

def cusignin(request):
    return render(request,"cusignin.html")

def checkcusignin(request): 
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        print(email)
        print(password)
        flag=Cusignup.objects.filter(Q(email__iexact=email) & Q(password__iexact=password))
        if flag:
            request.session['email']=email
            return redirect(cuhome)
        else:
            return render(request,"signupfail.html")
    else:
        return render(request,"cusignin.html")

def cuhome(request):
    if request.session.get("email",None):
        email=request.session["email"]
        result=Cusignup.objects.filter(email=email)
        count=Cuitems.objects.filter(email=email,cart="1").count()
        return render(request,"cuhome.html",{"result":result,"count":count})
    else:
        return redirect(cusignin)
    
def cuform(request):
    if request.session.get("email",None):
        email=request.session["email"]
        result=Cusignup.objects.filter(email=email)
        count=Cuitems.objects.filter(email=email,cart="1").count()
        return render(request,"cuform.html",{"result":result,"count":count})
    else:
        redirect(cusignin)

keycuitems=None
def cuformcheck(request):
    if request.session.get("email",None):
        if request.method=="POST":
            clothgender=request.POST['clothgender']
            clothtype=request.POST['clothtype']
            clothcolour=request.POST['clothcolour'] 
            clothpattern=request.POST['clothpattern']
            clothsizes=request.POST['clothsizes']
            result=Fdform.objects.filter(clothtype=clothtype,clothcolour=clothcolour,clothpattern=clothpattern,clothsizes=clothsizes,clothgender=clothgender)
            if result:
                global keycuitems
                def keycuitems():
                    return result
                return redirect("cuitems")
            else:
                return redirect("cuform")
        else:
            return render(request,'cuform.html')
    else:
        return redirect(cusignin)

def cuitems(request):
    if request.session.get("email",None):
        result=keycuitems()
        return render(request,'cuitems.html',{"result":result,'media_url':settings.MEDIA_URL})
    else:
        return redirect(cusignin)

keycuitemid=None
def curesult(request,id):
    if request.session.get("email",None):
        result=Fdform.objects.filter(id=id)
        global keycuitemid
        def keycuitemid():
            return id
        return render(request,"curesult.html",{"result":result,'media_url':settings.MEDIA_URL})
    else:
        return redirect(cusignin)

def cusaveitems(request):
    if request.session.get("email",None):
        id=keycuitemid()
        email=request.session["email"]
        clothname= Fdform.objects.filter(id=id).values('clothname')[0]['clothname']
        clothfile= Fdform.objects.filter(id=id).values('clothfile')[0]['clothfile']
        clothgender= Fdform.objects.filter(id=id).values('clothgender')[0]['clothgender']
        clothtype= Fdform.objects.filter(id=id).values('clothtype')[0]['clothtype']
        clothcolour= Fdform.objects.filter(id=id).values('clothcolour')[0]['clothcolour']
        clothpattern= Fdform.objects.filter(id=id).values('clothpattern')[0]['clothpattern']
        clothsizes= Fdform.objects.filter(id=id).values('clothsizes')[0]['clothsizes']
        clothprice= Fdform.objects.filter(id=id).values('clothprice')[0]['clothprice']
        clothdesigner= Fdform.objects.filter(id=id).values('username')[0]['username']
        username=Cusignup.objects.filter(email=email).values('username')[0]['username']

        flag=Cuitems.objects.filter(clothname=clothname,email=email)
        if flag:
            Cuitems.objects.filter(clothname=clothname,email=email).update(cart="1")
            return redirect(cushoppinglist)
        else:
            data=Cuitems(clothdesigner=clothdesigner,clothname=clothname,clothfile=clothfile,clothgender=clothgender,clothtype=clothtype,clothcolour=clothcolour,clothpattern=clothpattern,clothsizes=clothsizes,clothprice=clothprice,username=username,email=email,cart="1")
            data.save()
            return redirect(cushoppinglist)
    else:
        return redirect(cusignin)

def cushoppinglist(request):
    if request.session.get("email",None):
        email=request.session["email"]
        username=Cusignup.objects.filter(email=email).values('username')[0]['username']
        result=Cuitems.objects.filter(email=email,cart="1")
        count=Cuitems.objects.filter(email=email,cart="1").count()
        tp=0
        for i in range(0, count):
            tp=tp+Cuitems.objects.filter(email=email,cart="1").values('clothprice')[i]['clothprice']
        return render(request, "cushoppinglist.html",{"result":result,"tp":tp,"count":count,"username":username,'media_url':settings.MEDIA_URL})
    else:
        return redirect("cusignin")

def cucartdeleteitem(request,id):
    flag=Cuitems.objects.filter(id=id,cart="1",wishlist="0",order="0")
    if flag:
        Cuitems.objects.filter(id=id).delete()
    else:
        Cuitems.objects.filter(id=id).update(cart="0")
    return redirect(cushoppinglist)

def cusavewishlist(request):
    if request.session.get("email",None):
        id=keycuitemid()
        email=request.session["email"]
        clothname= Fdform.objects.filter(id=id).values('clothname')[0]['clothname']
        clothfile= Fdform.objects.filter(id=id).values('clothfile')[0]['clothfile']
        clothgender= Fdform.objects.filter(id=id).values('clothgender')[0]['clothgender']
        clothtype= Fdform.objects.filter(id=id).values('clothtype')[0]['clothtype']
        clothcolour= Fdform.objects.filter(id=id).values('clothcolour')[0]['clothcolour']
        clothpattern= Fdform.objects.filter(id=id).values('clothpattern')[0]['clothpattern']
        clothsizes= Fdform.objects.filter(id=id).values('clothsizes')[0]['clothsizes']
        clothprice= Fdform.objects.filter(id=id).values('clothprice')[0]['clothprice']
        clothdesigner= Fdform.objects.filter(id=id).values('username')[0]['username']
        username=Cusignup.objects.filter(email=email).values('username')[0]['username']
        flag=Cuitems.objects.filter(clothname=clothname,email=email)
        if flag:
            Cuitems.objects.filter(clothname=clothname,email=email).update(wishlist="1")
            return redirect(cuwishlist)
        else:
            data=Cuitems(clothdesigner=clothdesigner,clothname=clothname,clothfile=clothfile,clothgender=clothgender,clothtype=clothtype,clothcolour=clothcolour,clothpattern=clothpattern,clothsizes=clothsizes,clothprice=clothprice,username=username,email=email,wishlist="1")
            data.save()
            return redirect(cuwishlist)
    else:
        return redirect("cusignin")

def cuwishlist(request):
    if request.session.get("email",None):
        email=request.session["email"]
        username= Cusignup.objects.filter(email=email).values('username')[0]['username']
        result=Cuitems.objects.filter(email=email,wishlist="1")
        count=Cuitems.objects.filter(email=email,cart="1").count()
        return render(request, "cuwishlist.html",{"result":result,'media_url':settings.MEDIA_URL,"count":count,"username":username})
    else:
        return redirect(cusignin)

def cuwishlistdeleteitem(request,id):
    flag=Cuitems.objects.filter(id=id,cart="0",wishlist="1",order="0")
    if flag:
        Cuitems.objects.filter(id=id).delete()
    else:
        Cuitems.objects.filter(id=id).update(wishlist="0")
    return redirect(cuwishlist)

def cuwishlisttocart(request,id):
    Cuitems.objects.filter(id=id).update(cart="1")
    return redirect(cushoppinglist)

def cuviewitem(request,id):
    if request.session.get("email",None):
        result=Cuitems.objects.filter(id=id)
        return render(request,"cuviewitem.html",{"result":result,'media_url':settings.MEDIA_URL})
    else:
        return redirect(cusignin)

def culogout(request):
    del request.session["email"]
    return redirect(cupage)

def cucontactus(request):
    return render(request,'cucontactus.html')

def cusearchoutfit(request):
    if request.session.get("email",None):
        if request.method=="POST":
            outfit_name=request.POST['outfit_name']
            result=Fdform.objects.filter(clothname=outfit_name)
            if result:
                return render(request,'cufsearch.html',{"result":result,'media_url':settings.MEDIA_URL})
            else:
                return render(request,'cuform.html')
        else:
            return render(request,'cuform.html')
    else:
        return redirect(cusignin)

def cuorders(request):
    email=request.session["email"]
    result=Cuitems.objects.filter(email=email,order="1")
    count=Cuitems.objects.filter(email=email,order="1").count()
    tp=0
    for i in range(0, count):
        tp=tp+Cuitems.objects.filter(email=email,order="1").values('clothprice')[i]['clothprice']
    return render(request, "cuorders.html",{"result":result,"tp":tp,'media_url':settings.MEDIA_URL})
