from django.db import models

class Class(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
