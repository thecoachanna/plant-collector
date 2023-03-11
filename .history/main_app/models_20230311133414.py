from django.db import models

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=100, default=)
    type = models.CharField(max_length=100, default='')
    description = models.TextField(max_length=250, default='')

    # dunder str method return plant name
    def __str__(self):
        return self.name