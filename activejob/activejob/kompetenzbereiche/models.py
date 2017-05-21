from django.db import models

class Job(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return name

class Bereich(models.Model):
    title = models.CharField(max_length=200)
    jobs = models.ForeignKey("Job")

    def __str__(self):
        return title


class Kompetenzbereiche(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200)
    text = models.CharField(max_length=1000)
    fields = models.ForeignKey("Bereich")
    banner_color = models.CharField(max_length=6)
    banner_slogan = models.CharField(max_length=200)
    slug = models.CharField(max_length=100)
