from django.core.urlresolvers import reverse
from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def imageurl(self):
        return "{}.{}.jpg".format(self.first_name, self.last_name)


class ContactProfile(models.Model):
    status = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    mail = models.EmailField()
    priority = models.DecimalField(max_digits=2, decimal_places=0)
    location = models.ForeignKey("Location")
    contact = models.ForeignKey("Contact")

    def __str__(self):
        return "{} ({})".format(self.contact, self.status)

    class Meta:
        ordering = ["-priority"]

    # proxy:
    def first_name(self):
        return self.contact.first_name

    def last_name(self):
        return self.contact.last_name

    def imageurl(self):
        return self.contact.imageurl


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

    contact_profile = models.ForeignKey("ContactProfile")
    company = models.ForeignKey("Company")
    department = models.ForeignKey("Department")

    states = models.ManyToManyField("State")
    categories = models.ManyToManyField("Category")

    def __str__(self):
        return "{} ({}) {}".format(self.title, self.location, self.pk)

    def get_absolute_url(self):
        return reverse("job_detail", args=[self.pk, self.slug])

    class Meta:
        ordering = ["-changed_at"]


class Company(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = "companies"


class State(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"
        ordering = ["name"]


class Department(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
