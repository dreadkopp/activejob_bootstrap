from django.db import models

class Ansprechpartner(models.Model):
    title = models.CharField(max_length=150)
    field = models.CharField(max_length=100)
    banner_color = models.CharField(max_length=6)
    banner_slogan = models.CharField(max_length=200)
    contacts = models.ManyToManyField(Contact)

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    mail = models.EmailField()

    location = models.ForeignKey("Location")

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def imageurl(self):
        return "{}.{}.jpg".format(self.first_name, self.last_name)
