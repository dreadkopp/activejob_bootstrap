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

from django.conf.urls import url
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

from jobs.views import JobDetailView, JobListView

def placeholder():
    return TemplateView.as_view(template_name="web/pages/home")


urlpatterns = [
    url(r"^jobs/",
        JobListView.as_view(),
        name="stellenmarkt"
    ),

    url(r"^job/(?P<pk>\d+)$",
        JobDetailView.as_view(),
        name="job_detail"
    ),
    url(r"^kontakt",TemplateView.as_view(template_name="web/pages/kontakt.html"),name="kontakt"),
    url(r"^sitemap",placeholder(),name="sitemap"),
    url(r"^impressum",TemplateView.as_view(template_name="web/pages/impressum.html"),name="impressum"),
    url(r"^unternehmensprofil",TemplateView.as_view(template_name="web/pages/unternehmensprofil.html"),name="unternehmensprofil"),
    url(r"^jobs_rss",placeholder(),name="jobs_rss"),
    url(r"^$",TemplateView.as_view(template_name="web/pages/home.html"),name="home"),
    url(r"^leitbild",TemplateView.as_view(template_name="web/pages/leitbild.html"),name="leitbild"),
    url(r"^standorte",TemplateView.as_view(template_name="web/pages/standorte.html"),name="standorte"),
    url(r"^arbeitnehmerueberlassung",TemplateView.as_view(template_name="web/pages/arbeitnehmerueberlassung.html"),name="arbeitnehmerueberlassung"),
    url(r"^personalvermittlung",TemplateView.as_view(template_name="web/pages/personalvermittlung.html"),name="personalvermittlung"),
    url(r"^arbeitsvermittlung",TemplateView.as_view(template_name="web/pages/arbeitsvermittlung.html"),name="arbeitsvermittlung"),
    url(r"^personalanfrage",TemplateView.as_view(template_name="web/pages/personalanfrage.html"),name="personalanfrage"),
    url(r"^personalauswahl",TemplateView.as_view(template_name="web/pages/personalauswahl.html"),name="personalauswahl"),
    url(r"^bewerber_zeitarbeit",TemplateView.as_view(template_name="web/pages/bewerber_zeitarbeit.html"),name="bewerber_zeitarbeit"),
    url(r"^bewerber_personalvermittlung",TemplateView.as_view(template_name="web/pages/bewerber_personalvermittlung.html"),name="bewerber_personalvermittlung"),
    url(r"^bewerber_arbeitsvermittlung_antworten",TemplateView.as_view(template_name="web/pages/bewerber_arbeitsvermittlung_antworten.html"),name="bewerber_arbeitsvermittlung_antworten"),
    url(r"^bewerber_arbeitsvermittlung",TemplateView.as_view(template_name="web/pages/bewerber_arbeitsvermittlung.html"),name="bewerber_arbeitsvermittlung"),
    url(r"^karriereberatung",TemplateView.as_view(template_name="web/pages/karriereberatung.html"),name="karriereberatung"),
    url(r"^karriere_activjob",TemplateView.as_view(template_name="web/pages/karriere_activjob.html"),name="karriere_activjob"),
#    view(r'^$'),
#    view(r'^arbeitnehmerueberlassung'),
#    view(r'^arbeitsvermittlung_kompetenzbereiche'),
#    view(r'^arbeitsvermittlung_ansprechpartner'),
#    view(r'^arbeitsvermittlung'),
#    view(r'^bewerber_arbeitsvermittlung_vorteile'),
#    view(r'^bewerber_arbeitsvermittlung_berufsfelder'),
#    view(r'^bewerber_arbeitsvermittlung_antworten'),
#    view(r'^bewerber_arbeitsvermittlung_ansprechpartner'),
#    view(r'^bewerber_arbeitsvermittlung'),
#    view(r'^bewerber_personalvermittlung_vorteile'),
#    view(r'^bewerber_personalvermittlung_berufsfelder'),
#    view(r'^bewerber_personalvermittlung_ansprechpartner'),
#    view(r'^bewerber_personalvermittlung'),
#    view(r'^bewerber_zeitarbeit_vorteile'),
#    view(r'^bewerber_zeitarbeit_berufsfelder'),
#    view(r'^bewerber_zeitarbeit_ansprechpartner'),
#    view(r'^bewerber_zeitarbeit'),
#    view(r'^bewerber'),
#    view(r'^home'),
#    view(r'^impressum'),
#    view(r'^karriere_activjob'),
#    view(r'^karriereberatung'),
#    view(r'^kontakt'),
#    view(r'^leitbild'),
#    view(r'^personalauswahl'),
#    view(r'^personalanfrage'),
#    view(r'^personalvermittlung_referenzen'),
#    view(r'^personalvermittlung_kompetenzbereiche'),
#    view(r'^personalvermittlung_ansprechpartner'),
#    view(r'^personalvermittlung'),
#    view(r'^sitemap'),
#    view(r'^standorte'),
#    view(r'^standort'),
#    view(r'^stellenmarkt'),
#    view(r'^unternehmensprofil'),
#    view(r'^unternehmen'),
#    view(r'^zeitarbeit_kompetenzbereiche'),
#    view(r'^zeitarbeit_ansprechpartner'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
