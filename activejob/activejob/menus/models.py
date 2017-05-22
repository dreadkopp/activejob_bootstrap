from django.db import models

# Create your models here.
class MenuItem:
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    active = models.BooleanField
    sublist = models.ForeignKey(MenuItem)

class TopMenu:
    menuItems = models.ForeignKey(MenuItem)

    __str__(self):
        return menuItems

class LeftMenu:
    menuItems ) models.ForeignKey(MenuItem)

    __str__(self):
        return menuItems
