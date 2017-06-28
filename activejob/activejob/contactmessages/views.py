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
