from django.shortcuts import render
from django.contrib import messages

def index(request):
    return render(
        request=request,
        context={},
        template_name="home/index.html",
    ) 
    
    