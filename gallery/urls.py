from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views


urlpatterns=[
    path('',views.welcome, name = 'welcome'),
    path('image/(<category_name>\w+)/(<image_id>\d+)',views.by_image, name = 'by_image'),
    path('search/',views.search, name = 'search_image'),
    path('location/(<image_location>\d+)',views.filter_by_location, name = 'location')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)