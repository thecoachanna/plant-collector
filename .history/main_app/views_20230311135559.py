from django.shortcuts import render
from .models import Plant

# temporary plants for building templates
plants = [
    {'name': 'Monstera', 'type': 'Tropical', 'instructions': "Monsteras prefer soil that is lightly moist, and generally like to dry out a little bit between waterings. As epiphytes with aerial roots, they are sensitive to overwatering, so they don't want to sit in soggy soil. Once the top 2 to 4 inches of the soil are dry, your plant might use a drink."},
    {'name': 'Cactus', 'type': 'Desert', 'instructions': "Water every 1-2 weeks, depending on the temperature. When the temperatures rise to 90+ degrees reduce watering to every two weeks. Plants go dormant when the temperature is too high and can survive on the water they have stored. In late fall and winter, reduce watering to once every 3-4 weeks."}
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
    # pass data to our templates through view functions - gather relations from SQL using model methods
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', {'plants': plants})
