from itertools import product
from django.urls import path
from . import views

urlpatterns = [
    path('',views.userLogin, name = 'login'),
    path('orm',views.ormExample),
    path('logout',views.userLogout),
    path('signup',views.createUser, name = 'signup'),
    path('important',views.impFunction),
    path('image',views.imageProcessing),
    path('products',views.homepage2),
    path('product/<value>',views.dynamicURL,name= 'product'),
    path('class',views.MyView.as_view())
]