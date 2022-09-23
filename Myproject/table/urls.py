from django.urls import path,include
from . import views

urlpatterns= [
    path('',views.table),
    path('table/',views.table),

]