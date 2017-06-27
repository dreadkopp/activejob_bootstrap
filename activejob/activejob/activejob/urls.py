"""activejob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from jobs.views import JobDetailView, JobInternListView, JobSearchListView, RSSFeed
from ansprechpartner.views import AnsprechpartnerView
from berufsfelder.views import BerufsfelderView
from core.utils import MenuMixin
from jobs.mixins import QuickSearchFormMixin
from kompetenzbereiche.views import KompetenzbereicheView
from vorteile.views import VorteileView
from standorte.views import StandorteView

def placeholder():
    return TemplateView.as_view(template_name="web/pages/home")


# TODO: move this stuff somewhere else
class TemplateView(QuickSearchFormMixin, MenuMixin, TemplateView):
    pass


urlpatterns = [
    url(
        r'^admin/',
        include(admin.site.urls),
    ),

    url(r"^jobs$",
        JobSearchListView.as_view(
            active_nodes={"top": "bewerber", "left": "stellenmarkt"},
        ),
        name="stellenmarkt"
    ),

    url(r"^[jJ]obs/(stellenmarkt-)?(?P<pk>\d+)_(?P<slug>.*)$",
        JobDetailView.as_view(
            active_nodes={"top": "bewerber", "left": "stellenmarkt"},
        ),
        name="job_detail"
    ),
    url(r"^test",TemplateView.as_view(template_name="web/test/test.html"), name="test"),

    url(
        r"^ansprechpartner/(?P<slug>\w+)$",
        AnsprechpartnerView.as_view(
            # TODO: change this dynamically (in the view?)
            active_nodes={"top": "bewerber", "left": "bewerber_zeitarbeit", "sub": "Ansprechpartner"},
        ),
        name="ansprechpartner",
    ),

    url(r"^berufsfelder/(?P<slug>\w+)$",BerufsfelderView.as_view(),name="berufsfelder"),
    url(r"^kompetenzbereiche/(?P<slug>\w+)$",KompetenzbereicheView.as_view(),name="kompetenzbereiche"),

    url(
        r"^vorteile/(?P<slug>\w+)$",
        VorteileView.as_view(
        ),
        name="vorteile",
    ),

    url(
        r"^kontakt$",
        TemplateView.as_view(
            active_nodes={"top": "unternehmensprofil", "left": "kontakt"},
            template_name="web/pages/kontakt.html",
        ),
        name="kontakt",
    ),

    url(r"^sitemap",placeholder(),name="sitemap"),

    url(
        r"^impressum$",
        TemplateView.as_view(
            active_nodes={"top": "unternehmensprofil"},
            template_name="web/pages/impressum.html",
        ),
        name="impressum",
    ),

    url(
        r"^unternehmensprofil$",
        TemplateView.as_view(
            active_nodes={"top": "unternehmensprofil", "left": "unternehmensprofil"},
            template_name="web/pages/unternehmensprofil.html",
        ),
        name="unternehmensprofil",
    ),

    url(
        r"^unternehmen$",
        TemplateView.as_view(
            active_nodes={"top": "unternehmen"},
            template_name="web/pages/unternehmen.html",
        ),
        name="unternehmen",
    ),

    url(
        r"^Jobs/Jobs.xml$",
        RSSFeed(),
        name="jobs_rss",
    ),

    url(
        r"^referenzen$",
        TemplateView.as_view(
            active_nodes={"top": "unternehmen", "left": "referenzen"},
            template_name="web/pages/referenzen.html",
        ),
        name="referenzen",
    ),

    url(
        r"^$",
        TemplateView.as_view(
            active_nodes={"top": "home"},
            template_name="web/pages/home.html",
        ),
        name="home",
    ),

    url(
        r"^leitbild$",
        TemplateView.as_view(
            active_nodes={"top": "unternehmensprofil", "left": "Leitbild"},
            template_name="web/pages/leitbild.html",
        ),
        name="leitbild",
    ),

    url(
        r"^standorte$",
        StandorteView.as_view(
            active_nodes={"top": "unternehmensprofil", "left": "standorte"},
            template_name="web/pages/standorte.html",
        ),
        name="standorte",
    ),

    url(r"^arbeitnehmerueberlassung$",
        TemplateView.as_view(
            active_nodes={"top": "unternehmen", "left": "arbeitnehmerueberlassung"},
            template_name="web/pages/arbeitnehmerueberlassung.html",
        ),
        name="arbeitnehmerueberlassung",
    ),

    url(r"^personalvermittlung_referenzen",TemplateView.as_view(template_name="web/pages/personalvermittlung_referenzen.html"),name="personalvermittlung_referenzen"),

    url(
        r"^personalvermittlung$",
        TemplateView.as_view(
            active_nodes={"top": "unternehmen", "left": "personalvermittlung"},
            template_name="web/pages/personalvermittlung.html",
        ),
        name="personalvermittlung",
    ),

    url(
        r"^arbeitsvermittlung$",
        TemplateView.as_view(
            active_nodes={"top": "unternehmen", "left": "arbeitsvermittlung"},
            template_name="web/pages/arbeitsvermittlung.html",
        ),
        name="arbeitsvermittlung",
    ),

    url(
        r"^personalanfrage$",
        TemplateView.as_view(
            active_nodes={"top": "unternehmen", "left": "personalanfrage"},
            template_name="web/pages/personalanfrage.html",
        ),
        name="personalanfrage",
    ),

    url(
        r"^personalauswahl$",
        TemplateView.as_view(
            active_nodes={"top": "unternehmen", "left": "personalauswahl"},
            template_name="web/pages/personalauswahl.html",
        ),
        name="personalauswahl",
    ),

    url(
        r"^bewerber_zeitarbeit$",
        TemplateView.as_view(
            active_nodes={"top": "bewerber", "left": "bewerber_zeitarbeit"},
            template_name="web/pages/bewerber_zeitarbeit.html",
        ),
        name="bewerber_zeitarbeit",
    ),

    url(
        r"^bewerber_personalvermittlung$",
        TemplateView.as_view(
            active_nodes={"top": "bewerber", "left": "bewerber_personalvermittlung"},
            template_name="web/pages/bewerber_personalvermittlung.html",
        ),
        name="bewerber_personalvermittlung",
    ),

    url(
        r"^bewerber_arbeitsvermittlung_antworten$",
        TemplateView.as_view(
            active_nodes={"top": "bewerber", "left": "bewerber_arbeitsvermittlung", "sub": "bewerber_arbeitsvermittlung_antworten"},
            template_name="web/pages/bewerber_arbeitsvermittlung_antworten.html",
        ),
        name="bewerber_arbeitsvermittlung_antworten",
    ),

    url(
        r"^bewerber_arbeitsvermittlung$",
        TemplateView.as_view(
            active_nodes={"top": "bewerber", "left": "bewerber_arbeitsvermittlung"},
            template_name="web/pages/bewerber_arbeitsvermittlung.html",
        ),
        name="bewerber_arbeitsvermittlung",
    ),

    url(
        r"^bewerber$",
        TemplateView.as_view(
            active_nodes={"top": "bewerber"},
            template_name="web/pages/bewerber.html",
        ),
        name="bewerber",
    ),

    url(
        r"^karriereberatung$",
        TemplateView.as_view(
            active_nodes={"top": "bewerber", "left": "karriereberatung"},
            template_name="web/pages/karriereberatung.html",
        ),
        name="karriereberatung",
    ),

    url(
        r"^karriere_activjob$",
        JobInternListView.as_view(
            active_nodes={"top": "bewerber", "left": "karriere_activjob"},
        ),
        name="karriere_activjob",
    ),
]
