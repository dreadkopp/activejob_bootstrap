import json

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import Confirmation, PendingConfirmation
from core.views import SearchAndMenuCreateView


class ConfirmationCreateView(SearchAndMenuCreateView):
    model = Confirmation
    fields = []
    success_url = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        self.pending_confirmation = get_object_or_404(
            PendingConfirmation,
            slug=kwargs["slug"]
        )

        if self.pending_confirmation.has_expired():
            msg = "Dieser Bestätigungslink ist nicht mehr gültig."
            messages.error(request, msg)
            return redirect("home")

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.pending_confirmation = self.pending_confirmation
        logdata = {
            k: v
            for k, v in self.request.environ.items()
            if k.startswith("HTTP")
        }
        form.instance.logdata = json.dumps(logdata, indent=2)

        msg = "Vielen Dank!"
        messages.success(self.request, msg)

        return super().form_valid(form)
