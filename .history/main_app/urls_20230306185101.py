from django.urls import path
from . import views

urlpatterns = [
    # using an empty string makes this the root route
    # views.home refers to a view that renders a file
    # the name='home' kwarg gives the route a name
    # naming routes is optional but best practice
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path for plants
    path('plants/', views.plants_index, name='index')
]