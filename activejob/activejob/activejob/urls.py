from django.conf.urls import include, url
from django.contrib import admin

from contactmessages.views import ContactMessageView
from contactmessages.views import PersonalanfrageView
from core.views import SearchAndMenuTemplateView as TemplateView, SitemapView
from jobs.views import JobDetailView, JobInternListView, JobSearchListView, RSSFeed
from ansprechpartner.views import AnsprechpartnerView
from berufsfelder.views import BerufsfelderView
from kompetenzbereiche.views import KompetenzbereicheView
from vorteile.views import VorteileView
from standorte.views import StandorteView
from referenzen.views import ReferenzenView, ReferenzenBlingView
from pages.models import Page
from pages.views import PageView, homepage
from django.views.generic import RedirectView
from core.utils import fix_stellenmarkt_links

class Dummy(TemplateView):
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

    url(
        r"^ansprechpartner/(:?(?P<variant>\w+)/)?(?P<slug>\w+)$",
        AnsprechpartnerView.as_view(
        ),
        name="ansprechpartner",
    ),

    url(
        r"^berufsfelder/(?P<slug>\w+)$",
        BerufsfelderView.as_view(
        ),
        name="berufsfelder",
    ),

    url(
        r"^kompetenzbereiche/(?P<slug>\w+)$",
        KompetenzbereicheView.as_view(
        ),
        name="kompetenzbereiche"
    ),

    url(
        r"^vorteile/(?P<slug>\w+)$",
        VorteileView.as_view(
        ),
        name="vorteile",
    ),

    url(
        r"^kontakt$",
        ContactMessageView.as_view(
            active_nodes={"top": "unternehmensprofil", "left": "kontakt"},
        ),
        name="kontakt",
    ),

    url(r"^sitemap$",
        SitemapView.as_view(
            active_nodes={"top": "home", "left": "unternehmensprofil"},
            template_name="web/pages/sitemap.html",
        ),
        name="sitemap",
    ),

    url(
        r"^Jobs/Jobs.xml$",
        RSSFeed(),
        name="jobs_rss",
    ),

    url(
        r"^referenzen/(?P<slug>\w+)/aktuell$",
        ReferenzenBlingView.as_view(
        ),
        name="referenzen_aktuell",
    ),

    url(
        r"^referenzen/(?P<slug>\w+)$",
        ReferenzenView.as_view(
        ),
        name="referenzen",
    ),

    url(
        r"^standorte$",
        StandorteView.as_view(
            active_nodes={"top": "unternehmensprofil", "left": "standorte"},
            template_name="web/pages/standorte.html",
        ),
        name="standorte",
    ),
    url(
        r"^personalanfrage$",
        PersonalanfrageView.as_view(
            active_nodes={"top": "unternehmen", "left": "personalanfrage"},
            template_name="web/pages/personalanfrage.html",
        ),
        name="personalanfrage",
    ),

    url(
        r"^karriere_activjob$",
        JobInternListView.as_view(
            active_nodes={"top": "bewerber", "left": "karriere_activjob"},
        ),
        name="karriere_activjob",
    ),

    url(
    	r"^$",
        homepage,
        name="home",
    ),

    url(
        r"(?P<slug>\w+)$",
        PageView.as_view(),
        name="page",
    ),
]

urlpatterns += [
    url(
        r"^{}$".format(page.slug),
        Dummy,
        name=page.slug,
    ) for page in Page.objects.all()
        if page.slug not in (
            pattern.name
            for pattern in urlpatterns
                if hasattr(pattern, "name")
        )
]

fix_stellenmarkt_links()
