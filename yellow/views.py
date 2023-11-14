from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def siri(request):
    return render(request,'siri.html')

def nani(request):
    return HttpResponse('<h1>this is nani</h1>')