from django.urls import path
from app1.views import *
app_name='ubese'
urlpatterns=[
    path('laddu/',laddu,name='laddu')
]