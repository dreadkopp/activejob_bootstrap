from django.db import models
from jobs.models import Location

class Locations(models.Model):
    locations = models.ForeignKey(Location)
