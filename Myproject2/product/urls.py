from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name = 'home'),
    path('grocery/',views.grocery, name = 'grocery'),
    path('fashion/',views.fashion, name = 'fashion'),
    path('electronics/',views.electronics, name = 'electronics'),
    path('toys/',views.toys, name = 'toys'),
    path('mobiles/',views.mobiles, name = 'mobiles'),
    path('pc/',views.personalcare, name = 'personalcare'),
    path('furnitures/',views.furnitures, name = 'furnitures'),
]