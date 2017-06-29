from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=64)
    subtitle = models.CharField(max_length=64)
    text = models.TextField(max_length=2000)
    banner_color = models.CharField(max_length=6)
    banner_slogan = models.CharField(max_length=128)
    slug = models.CharField(max_length=64)
