from django.db import models

class Kompetenzbereich(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200)
    text = models.CharField(max_length=1000)
    banner_color = models.CharField(max_length=6)
    banner_slogan = models.CharField(max_length=200)
    slug = models.CharField(max_length=100)

class Bereich(models.Model):
    title = models.CharField(max_length=200)
    competencefield = models.ForeignKey("Kompetenzbereich")

    def __str__(self):
        return title

class Job(models.Model):
    name = models.CharField(max_length=200)
    field = models.ForeignKey("Bereich")

    def __str__(self):
        return name
