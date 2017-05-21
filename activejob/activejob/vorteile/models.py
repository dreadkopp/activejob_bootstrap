from django.db import models

class Pro(models.Model):
    text = models.CharField(max_length=1000)

    def __str__(self):
        return text


class Vorteile(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200)
    text = models.CharField(max_length=1000)
    pros = models.ForeignKey("Pro")
    banner_color = models.CharField(max_length=6)
    banner_slogan = models.CharField(max_length=200)
    slug = models.CharField(max_length=100)
