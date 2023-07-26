from django.urls import path
from app1.views import *
app_name='nothing'

urlpatterns=[
    path('first1/',first1,name='first1'),
]