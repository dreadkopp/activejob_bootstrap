from django.db import models
from django.utils import timezone

from jobs.models import Company


class PendingConfirmation(models.Model):
    slug = models.SlugField(primary_key=True, max_length=64)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
    )
    expires_at = models.DateTimeField()

    def __str__(self):
        return self.slug

    def has_expired(self):
        return self.expires_at <= timezone.now()


class Confirmation(models.Model):
    pending_confirmation = models.ForeignKey(
        PendingConfirmation,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    logdata = models.TextField()

    def __str__(self):
        return self.pending_confirmation.slug
