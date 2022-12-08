from django.urls import path
from app2.views import *
app_name='suhel'
urlpatterns=[
    path('pandu/',pandu,name='pandu')
]