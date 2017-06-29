from django.contrib import admin

from .models import (
    Field,
    Job,
    Page,
)


admin.site.register(Field)
admin.site.register(Job)
admin.site.register(Page)
