# Plant Collector
Django app all about plants.

# To run app
pipenv shell
python3 manage.py shell
python3 manage.py runserver

## User Stories
- As a User, when I click the View All My Plants link, I want to see a page listing all of my plants.
- AAU, when I click on a plant in the plants list, I want to see a page that displays all the details for that plant.

## Routes
/plants Plants index to view all plants
/plants/:id show plants view one plant

### Development Steps

1. Start by adding the URL to urls.py
2. Create the view associated with that URL
3. Make the HTML template for that view
4. Add some functionality(UI) to quickly get to that template