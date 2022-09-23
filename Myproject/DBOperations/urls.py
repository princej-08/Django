from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name ='home'),
    path('select',views.fetchData, name='select'),
    path('insert',views.insertData, name ='insert'),
    path('orminsert',views.ormInsertData, name = 'orminsert'),
    path('ormselect',views.ormFetchData, name = 'ormselect'),
    path('form',views.formExp),

]