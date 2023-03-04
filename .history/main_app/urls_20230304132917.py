from django.urls import path
from . import views

urlpatterns = [
    # using an emptry string makes this the root route
    # views.home refers to a file to render
    # the name='home' kwarg gives the route a name
    # naming routes is optional but best practice
    path('', views.home, name='home'),
]