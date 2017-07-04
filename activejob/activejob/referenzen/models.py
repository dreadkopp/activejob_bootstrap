from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=64)
    subtitle = models.CharField(max_length=64)
    banner_color = models.CharField(max_length=6)
    banner_slogan = models.CharField(max_length=128)
    text = models.TextField(max_length=1000)
    slug = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class Field(models.Model):
    name = models.CharField(max_length=128)
    page = models.ForeignKey("Page", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Job(models.Model):
    name = models.CharField(max_length=128)
    fields = models.ForeignKey("Field", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
