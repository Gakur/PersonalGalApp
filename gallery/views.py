from django.shortcuts import render, redirect
from . models import location, category, image

# Create your views here.
def welcome(request):
    images = image.get_all_images()
    locations = location.objects.all()
    title = 'Welcome Page'
    return render(request, 'welcome.html', {"images": images}, {"locations": locations}, {"title": title})
    

