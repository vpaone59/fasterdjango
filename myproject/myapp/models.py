from django.db import models


# Create your models here.
class Animal(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
