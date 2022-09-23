
from django.urls import path,include
from . import views

urlpatterns = [
    path('first/',views.firstFun),
    path('second/',views.secondFun),
    path('third/',views.thirdFun),
]