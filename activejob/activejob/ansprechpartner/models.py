from django.db import models

class Ansprechpartner(models.Model):
    title = models.CharField(max_length=100)
