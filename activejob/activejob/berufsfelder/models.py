from django.db import models

class Berufsfelder(models.Model):
    title = models.CharField(max_length=150)
    subtitel = models.CharField(max_length=200)
    banner_color = models.CharField(max_length=6)
    banner_slogan = models.CharField(max_length=200)
    
