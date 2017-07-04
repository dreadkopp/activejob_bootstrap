from django.contrib import admin

from .models import (
    Category,
    Company,
    Contact,
    ContactProfile,
    Department,
    Job,
    Location,
    State,
)


class JobAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "location", "contact_profile", "changed_at"]
    ordering = ["pk"]
    list_filter = ["is_intern"]
    search_fields = ["title", "location"]


admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Contact)
admin.site.register(ContactProfile)
admin.site.register(Department)
admin.site.register(Job, JobAdmin)
admin.site.register(Location)
admin.site.register(State)
