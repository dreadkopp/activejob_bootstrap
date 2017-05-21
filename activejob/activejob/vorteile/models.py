from django.db import models

class Vorteile(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200)
    banner_color = models.CharField(max_length=6)
    banner_slogan = models.CharField(max_length=200)
