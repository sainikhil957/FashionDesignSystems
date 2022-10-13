from django.urls import path,include
from FashionDesigner import views

urlpatterns = [
    path('',views.index,name="index"),
    path('index/',views.index,name="index"),

    path('fdpage/',views.fdpage,name="fdpage"),
    path('fdsignup/',views.fdsignup,name="fdsignup"),
    path('fdregister/',views.fdregister,name="fdregister"),
    path('fdsignin/',views.fdsignin,name="fdsignin"),
    path('checkfdsignin/',views.checkfdsignin,name="checkfdsignin"),
    path('fdhome/',views.fdhome,name="fdhome"),
    path('fdform/',views.fdform,name="fdform"),
    path('fdformstore/',views.fdformstore,name="fdformstore"),
     path('fdfilesuccess/',views.fdfilesuccess,name="fdfilesuccess"),
    path('fdfiles/',views.fdfiles,name="fdfiles"),
    path('fdfiledelete/<int:id>',views.fdfiledelete,name="fdfiledelete"),
    path('fdfileview/<int:id>',views.fdfileview,name="fdfileview"),
    path('fdcontactus',views.fdcontactus,name="fdcontactus"),
    path('fdlogout',views.fdlogout,name="fdlogout"),

    #path('',include('Customer.urls')),
]