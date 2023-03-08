from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def game(request):
    return HttpResponse('when a man running collecting the coins some creature is huntting ')
def man(request):
     return HttpResponse('<h1>select a icon which do you want to run</h1>')
def coins(request):
     return HttpResponse('<h1>total no of coins to collected</h1>')
