from django.db import models

class Berufsfelder(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(max_length=1000)
    banner_color = models.CharField(max_length=6)
    banner_slogan = models.CharField(max_length=200)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name_plural = "Berufsfelder"

class Bereich(models.Model):
    page = models.ForeignKey("Berufsfelder")
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Bereiche"


class Detail(models.Model):
    sector = models.ForeignKey("Bereich")
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
