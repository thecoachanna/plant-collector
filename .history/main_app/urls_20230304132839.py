from django.urls import path
from . import views

urlpatterns = [
    # using an emptry sting makes this the root route
    # views.home refers to a file to render
    
    path('', views.home, name='home'),
]