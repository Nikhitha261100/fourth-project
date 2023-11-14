from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def  indu(request):
    return render(request,'indu.html')

def bharathi(request):
    return HttpResponse('<h1>this is bharathi</h1>')