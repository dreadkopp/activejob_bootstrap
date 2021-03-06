from django.contrib import messages
from django.urls import reverse_lazy

from .models import ContactMessage, Personalanfrage
from core.views import SearchAndMenuCreateView


class SuccessMessageMixin:
    def form_valid(self, form):
        msg = "Vielen Dank! Ihre Nachricht wurde gesendet."
        messages.success(self.request, msg)
        return super().form_valid(form)


class ContactMessageView(SuccessMessageMixin, SearchAndMenuCreateView):
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


class PersonalanfrageView(SuccessMessageMixin, SearchAndMenuCreateView):
    model = Personalanfrage
    template_name = "web/pages/personalanfrage.html"
    success_url = reverse_lazy("unternehmen")
    fields = [
        "company",
        "first_name",
        "name",
        "street",
        "city",
        "phone",
        "email",
        "job",
        "qualifications",
        "location",
        "from_date",
    ]
