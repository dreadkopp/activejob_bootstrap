from django.contrib import messages
from django.core.urlresolvers import reverse_lazy

from .models import ContactMessage
from core.views import SearchAndMenuCreateView

class ContactMessageView(SearchAndMenuCreateView):
    model = ContactMessage
    template_name = "web/pages/kontakt.html"
    success_url = reverse_lazy("home")
    fields = [
        "first_name",
        "name",
        "company",
        "email",
        "subject",
        "message",
    ]

    def form_valid(self, form):
        msg = "Vielen Dank! Ihre Nachricht wurde gesendet."
        messages.success(self.request, msg)
        return super().form_valid(form)
