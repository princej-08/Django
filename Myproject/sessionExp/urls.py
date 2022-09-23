from django.urls import path
from . import views

urlpatterns = [
    path('<prdid>',views.sesFunction),
]