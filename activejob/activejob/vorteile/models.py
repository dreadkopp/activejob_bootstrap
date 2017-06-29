from django.db import models


class Vorteile(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)
    banner_color = models.CharField(max_length=6)
    banner_slogan = models.CharField(max_length=200)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name_plural = "Vorteile"

class Pro(models.Model):
    text = models.CharField(max_length=1000)
    page = models.ForeignKey("Vorteile")

    def __str__(self):
        return self.text
