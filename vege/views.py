from django.shortcuts import render
from .models import *

# Create your views here.
def rescipe(request):
    if request.method == "POST":
        data = request.POST
        
        rescipe_image=request.FILES.get("rescipe_image")
        rescipe_name=data.get('rescipe_name')
        rescipe_description=data.get('rescipe_description')
        
        Rescipe.objects.create(
            rescipe_name = rescipe_name,
            rescipe_image = rescipe_image,
            rescipe_description = rescipe_description,
        )
       
        
        
    return render(request , "rescipe.html")