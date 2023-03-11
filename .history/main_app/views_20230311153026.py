from django.shortcuts import render
from .models import Plant

# Create your views here.
# View functions match URLs to code like Controllers in Express
# define home view function
def home(request):
    return render(request, 'home.html')

# define about view function
def about(request):
    return render(request, 'about.html')

# index route for plants
def plants_index(request):
    # pass data to our templates through view functions - gather relations from SQL using model methods
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', {'plants': plants})

# Detail route for plants
# plant_id is defined, expecting an integer in our url
def plants_detail(request, plant_id):
    plant = P