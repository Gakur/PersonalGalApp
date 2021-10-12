from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from . models import Location, Category, Image
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def welcome(request):
    image = Image.get_all_images()
    locations = Location.objects.all()
    title = 'Welcome Page'
    return render(request, 'welcome.html', {"image": image,"locations": locations,"title": title})

def by_image(request, image_id, category_name):
    image_category = Image.objects.filter(image_category__name = category_name)
    locations = Location.objects.all()
    title = 'Images Page'

    try:
        image = Image.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"image.html",{"locations": locations,"image_category":image_category,"title": title,"image": image})

def search(request):
    locations = Location.objects.all()
    categories = Category.objects.all()
    title = 'Get Images Page'
    if 'image_category' in request.GET and request.GET['image_category']:
        search_term = request.GET.get('image_category')
        found_results = Image.search_by_category(search_term)
        message = f"{search_term}"
        print(search_term)
        print(found_results)

        return render(request, 'search_image.html',{'title':title,'images': found_results, 'message': message, 'categories': categories, "locations":locations})
    else:
        message = 'You havent searched yet'
        return render(request, 'search_image.html',{"message": message})


def filter_by_location(request, image_location):
    locations = Location.objects.all()
    location = Location.get_location_id(image_location)
    images = Image.filter_by_location(image_location)
    title = f'{location} Photos'
    return render(request, 'image_location.html', {'title':title, 'images':images, 'locations':locations, 'location':location})
        