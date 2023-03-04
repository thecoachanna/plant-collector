from django.urls import path
from . import views

urlpatterns = [
    # using an emptry sting makes this the root route
    path('', views.home, name='home'),
]