
from django.db import models

class BooksList(models.Model):
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=5)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50)