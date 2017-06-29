from django.db import models
from jobs.models import Contact


class Ansprechpartner(models.Model):
    title = models.CharField(max_length=150)
    field = models.CharField(max_length=100)
    banner_color = models.CharField(max_length=6)
    banner_slogan = models.CharField(max_length=200)
    contacts = models.ManyToManyField(Contact)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Ansprechpartner"
