from django.contrib import admin

from .models import PendingConfirmation, Confirmation


admin.site.register(PendingConfirmation)
admin.site.register(Confirmation)
