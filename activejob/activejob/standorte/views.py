from django.views.generic import ListView

from core.utils import MenuMixin
from jobs.mixins import QuickSearchFormMixin
from jobs.models import Location


class StandorteView(QuickSearchFormMixin, MenuMixin, ListView):
    template_name = "web/pages/standorte.html"
    model = Location
