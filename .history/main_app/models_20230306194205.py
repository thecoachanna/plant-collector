from django.db import models

# Create your models here.
class Plant(models.Model):
    name: models.CharField(max_length=100)
    type: models.CharField(max_length=100)
    description: models.TextField(max_length=250)

    # dunder str method return plant name
    def __str__(self):
        eturn self.name