from django.urls import path,include
from Customer import views

urlpatterns = [
 
    path('cupage/',views.cupage,name="cupage"),
    path('cusignup/',views.cusignup,name="cusignup"),
    path('curegister/',views.curegister,name="curegister"),
    path('cusignin/',views.cusignin,name="cusignin"),
    path('checkcusignin/',views.checkcusignin,name="checkcusignin"),

    path('cuhome/',views.cuhome,name="cuhome"),
    path('cuform/',views.cuform,name="cuform"),
    path('cuformcheck/',views.cuformcheck,name="cuformcheck"),
    path('cuitems/',views.cuitems,name="cuitems"),
    path('curesult/<int:id>',views.curesult,name="curesult"),

    path('cusaveitems/',views.cusaveitems,name="cusaveitems"),
    path('cushoppinglist/',views.cushoppinglist,name="cushoppinglist"),
    path('cucartdeleteitem/<int:id>',views.cucartdeleteitem,name="cucartdeleteitem"),
    
    path('cusavewishlist',views.cusavewishlist,name="cusavewishlist"),
    path('cuwishlist',views.cuwishlist,name="cuwishlist"),
    path('cuwishlistdeleteitem/<int:id>',views.cuwishlistdeleteitem,name="cuwishlistdeleteitem"),
    path('cuwishlisttocart/<int:id>',views.cuwishlisttocart,name="cuwishlisttocart"),
    
    path('cuorders',views.cuorders,name="cuorders"),
    path('cuviewitem/<int:id>',views.cuviewitem,name="cuviewitem"),
    path('cucontactus',views.cucontactus,name="cucontactus"),
    path('culogout',views.culogout,name="culogout"),
]