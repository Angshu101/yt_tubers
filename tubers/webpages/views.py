from django.shortcuts import render
from django.http import HttpResponse
from .models import*

# Create your views here.
def home(request):
    sliders=Slider.objects.all()
    context={
        'sliders':sliders,
    }
    return render(request,'webpages/home.html',context)
def about(request):
    return render(request,'webpages/about.html')
def services(request):
    return render(request,'webpages/services.html')
def contact(request):
    return render(request,'webpages/contact.html')