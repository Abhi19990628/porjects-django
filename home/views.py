from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request , "home/index.html")

def akk(request):
    return HttpResponse("abhishek chutiya")
    
def abhi(request):
    return HttpResponse("<h1> hi thi is abhishek page </h1>")