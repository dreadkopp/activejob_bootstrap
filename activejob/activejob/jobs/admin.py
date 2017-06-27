from django.contrib import admin

from .models import (
    Category,
    Company,
    Contact,
    Department,
    Job,
    Location,
    State,
)


admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Contact)
admin.site.register(Department)
admin.site.register(Job)
admin.site.register(Location)
admin.site.register(State)
