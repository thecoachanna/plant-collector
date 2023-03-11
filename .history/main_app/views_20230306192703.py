from django.shortcuts import render

# temporary plants for building templates
plants = [
    {'name': 'Monstera', 'type': 'Tropical', 'instructions': 'Monsteras prefer soil that is lightly moist, and generally like to dry out a little bit between waterings. As epiphytes with aerial roots, they are sensitive to overwatering, so they don't want to sit in soggy soil. Once the top 2 to 4 inches of the soil are dry, your plant might use a drink.'},
    {'name': 'Cactus', 'type': 'Desert', 'instructions': ''}
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
