from django.db import models

# Create your models here.
class Plant(models.Model):
    name: models.CharField(max_length=100)
    type: models.Charfield(max_length=100)
    description