import warnings

from django.db import models
from jobs.models import ContactProfile


class Ansprechpartner(models.Model):
    title = models.CharField(max_length=150)
    field = models.CharField(max_length=100)
    banner_color = models.CharField(max_length=6)
    banner_slogan = models.CharField(max_length=200,blank=True)
    contact_profiles = models.ManyToManyField(ContactProfile)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Ansprechpartner"

    def contacts(self):
        warnings.warn(
            "Ansprechpartner.contacts() called",
            PendingDeprecationWarning
        )
        return self.contact_profiles
