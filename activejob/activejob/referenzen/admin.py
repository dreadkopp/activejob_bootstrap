from django.contrib import admin

from .models import (
    Field,
    Job,
)


admin.site.register(Field)
admin.site.register(Job)
