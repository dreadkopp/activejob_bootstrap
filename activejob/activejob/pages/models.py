from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=64)
    subtitle = models.CharField(max_length=64)
    text = models.TextField(max_length=4000)
    banner_color = models.CharField(max_length=6)
    banner_slogan = models.CharField(max_length=128,blank=True)
    menu_top_entry = models.CharField(max_length=64)
    menu_left_entry = models.CharField(max_length=64)
    menu_left_sub_entry = models.CharField(max_length=64)
    slug = models.CharField(max_length=64,blank=True)

    def __str__(self):
        return self.slug
