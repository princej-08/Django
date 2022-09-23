from django.urls import path,include
from . import views

urlpatterns = [
    path('prime/',views.primenumber),

]