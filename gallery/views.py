from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from . models import location, category, Image
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def welcome(request):
    image = Image.get_all_images()
    locations = location.objects.all()
    title = 'Welcome Page'
    return render(request, 'welcome.html', {"image": image}, {"locations": locations}, {"title": title})

def by_image(request, image_id, category_name):
    locations = location.objects.all()
    categories = Image.objects.filter(name = category_name)
    title = 'Images Page'

    try:
        image = Image.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"image.html",{"locations": locations}, {"categories": categories}, {"title": title}, {"image": image})

