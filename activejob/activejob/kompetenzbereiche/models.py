from django.db import models


class Kompetenzbereich(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)
    banner_color = models.CharField(max_length=6)
    banner_slogan = models.CharField(max_length=200)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name_plural = "Kompetenzbereiche"


class Bereich(models.Model):
    title = models.CharField(max_length=200)
    competencefield = models.ForeignKey("Kompetenzbereich", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Bereiche"


class Job(models.Model):
    name = models.CharField(max_length=200)
    field = models.ForeignKey("Bereich", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
