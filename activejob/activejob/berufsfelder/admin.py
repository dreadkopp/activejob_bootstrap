from django.contrib import admin

from .models import (
    Berufsfelder,
    Bereich,
    Detail,
)


admin.site.register(Berufsfelder)
admin.site.register(Bereich)
admin.site.register(Detail)
