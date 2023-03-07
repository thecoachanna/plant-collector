from django.shortcuts import render

# temporary plants for building templates
plants = [
    {'name': 'Monstera', 'type': 'Tropical'},
    {'name': 'Cactus', 'type': 'Desert'}
]

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
    return render(request, 'plants/index.html', {'plants': plants})
