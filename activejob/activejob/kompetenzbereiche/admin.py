from django.contrib import admin

from .models import (
    Kompetenzbereich,
    Bereich,
    Job,
)


admin.site.register(Kompetenzbereich)
admin.site.register(Bereich)
admin.site.register(Job)
