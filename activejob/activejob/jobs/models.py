from django.db import models


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


class Location(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)
    mail = models.EmailField()
    gmaps_iframe_href = models.CharField(max_length=999)

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    profile = models.TextField()
    perspective = models.TextField()
    is_intern = models.BooleanField()
    changed_at = models.DateTimeField()

    contact = models.ForeignKey("Contact")
    company = models.ForeignKey("Company")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-changed_at"]


class Company(models.Model):
    description = models.TextField()
