from django.db import models

# Create your models here.
class MenuItem:
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    active = models.BooleanField
    #sublist = models.ForeignKey(MenuItem)

class TopMenu:
    #menuItems = models.ForeignKey(MenuItem)

    def __str__(self):
        return menuItems

class LeftMenu:
    #menuItems = models.ForeignKey(MenuItem)

    def __str__(self):
        return menuItems


#generate Menus something like this:

# check URL

#if only TopMenu URL > LeftMenu nothing active , TopMenu active Point X

#if LeftMenu selected > set related TopMenu Point active + Set currect URL MenuEntry active + If current MenuEntry is in Sublist set ancestor active as well
