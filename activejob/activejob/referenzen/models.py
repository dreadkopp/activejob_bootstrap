from django.db import models

class Job(models.Model):
    name = models.CharField(max_length=150)

class Field(models.Model):
    name = models.CharField(max_length=150)
    jobs = models.ForeignKey("Job")
