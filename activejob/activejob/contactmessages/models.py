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

class Personalanfrage(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    company = models.CharField("Firma", max_length=64, blank=True)
    first_name = models.CharField("Vorname", max_length=64)
    name = models.CharField(max_length=64)
    street = models.CharField("Straße/Hausnummer", max_length=64)
    city = models.CharField("PLZ/Ort", max_length=64)
    phone = models.CharField("Telefon", max_length=64)
    email = models.EmailField("E-Mail")
    job = models.CharField("Bedarf/Beruf")
    qualitications = models.CharField("Zusatzqualifikationen")
    location = models.CharField("Einsatzort/Gebiet")
    from_date = models.DateField

    def __str__ (self):
        return "{} {}".format(self.company, self.job)
