from django.db import models
from kompetenzbereiche.models import Job,Bereich

class Berufsfelder(models.Model):
    title = models.CharField(max_length=150)
    text = models.CharField(max_length=1000)
    fields = models.ForeignKey("Bereich")
    banner_color = models.CharField(max_length=6)
    banner_slogan = models.CharField(max_length=200)
    slug = models.CharField(max_length=100)
