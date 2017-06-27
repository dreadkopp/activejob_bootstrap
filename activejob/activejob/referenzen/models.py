from django.db import models

class Field(models.Model):
    name = models.CharField(max_length=150)

class Job(models.Model):
    name = models.CharField(max_length=150)
    field = models.ForeignKey("Field")
