from django.db import models

class Field(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Job(models.Model):
    name = models.CharField(max_length=150)
    fields = models.ForeignKey("Field")

    def __str__(self):
        return self.name
