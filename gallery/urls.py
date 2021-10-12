from django.urls import path
from django.conf.urls.static import static
from . import views


urlpatterns=[
    path('',views.welcome, name = 'welcome'),
    path('image/',views.by_image, name = 'by_image'),
    path('search/',views.search, name = 'search_image'),
    path('location/(\d+)',views.filter_by_location, name = 'filter_by_location')
]