from django.db import models

class Berufsfelder(models.Model):
    title = models.CharField(max_length=150)
    text = models.CharField(max_length=1000)
    banner_color = models.CharField(max_length=6)
    banner_slogan = models.CharField(max_length=200)
    slug = models.CharField(max_length=100)

class Bereich(models.Model):
    page = models.ForeignKey("Berufsfelder")
    name = models.CharField(max_length=200)


class Detail(models.Model):
    sector = models.ForeignKey("Bereich")
    name = models.CharField(max_length=200)
