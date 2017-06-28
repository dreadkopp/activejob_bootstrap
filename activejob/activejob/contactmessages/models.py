from django.db import models


class ContactMessage(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField("Vorname", max_length=64)
    name = models.CharField(max_length=64)
    company = models.CharField("Firma", max_length=64, blank=True)
    email = models.EmailField("E-Mail")
    subject = models.CharField("Betreff", max_length=64)
    message = models.TextField("Mitteilung")

    def __str__ (self):
        return "{} {}".format(self.first_name, self.name)
