from django.db import models
from django.urls import reverse


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
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    contact = models.ForeignKey("Contact", on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({})".format(self.contact, self.status)

    class Meta:
        ordering = ["contact__last_name", "contact__first_name", "pk"]

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
    slug = models.SlugField(max_length=255)
    location = models.CharField(max_length=100)
    description = models.TextField()
    profile = models.TextField()
    perspective = models.TextField()
    is_intern = models.BooleanField()
    changed_at = models.DateTimeField()

    contact_profile = models.ForeignKey("ContactProfile", on_delete=models.CASCADE)
    company = models.ForeignKey("Company", on_delete=models.CASCADE)
    department = models.ForeignKey("Department", on_delete=models.CASCADE)

    states = models.ManyToManyField("State")
    categories = models.ManyToManyField("Category")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("job_detail", args=[self.pk, self.slug])

    class Meta:
        ordering = ["-changed_at"]


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "companies"
        ordering = ["name", "pk"]


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
