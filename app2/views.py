from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first1(request):
    return HttpResponse('<h1>GOOD GIRL HARSH</h1>')