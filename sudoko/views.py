from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def numbers(request):
    return HttpResponse('<h1> we have arrange numbers<h1>')
def box(request):
    return HttpResponse('<h1> we have arrange numbers 1 to 9</h1>')