from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('login/',login,name='login'),
    path('logindata/',logindata,name='logindata'),
    path('dashboard/',dashboard,name='dashboard')

]
