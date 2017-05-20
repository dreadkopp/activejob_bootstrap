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
    url(r"^referenzen",TemplateView.as_view(template_name="web/pages/referenzen.html"),name="referenzen"),
    url(r"^$",TemplateView.as_view(template_name="web/pages/home.html"),name="home"),
    url(r"^leitbild",TemplateView.as_view(template_name="web/pages/leitbild.html"),name="leitbild"),
    url(r"^standorte",TemplateView.as_view(template_name="web/pages/standorte.html"),name="standorte"),
    url(r"^arbeitnehmerueberlassung",TemplateView.as_view(template_name="web/pages/arbeitnehmerueberlassung.html"),name="arbeitnehmerueberlassung"),
    url(r"^personalvermittlung_referenzen",TemplateView.as_view(template_name="web/pages/personalvermittlung_referenzen.html"),name="personalvermittlung_referenzen"),
    url(r"^personalvermittlung_kompetenzbereiche",TemplateView.as_view(template_name="web/pages/personalvermittlung_kompetenzbereiche.html"),name="personalvermittlung_kompetenzbereiche"),
    url(r"^personalvermittlung_ansprechpartner",TemplateView.as_view(template_name="web/pages/personalvermittlung_ansprechpartner.html"),name="personalvermittlung_ansprechpartner"),
    url(r"^personalvermittlung",TemplateView.as_view(template_name="web/pages/personalvermittlung.html"),name="personalvermittlung"),
    url(r"^arbeitsvermittlung_kompetenzbereiche",TemplateView.as_view(template_name="web/pages/arbeitsvermittlung_kompetenzbereiche.html"),name="arbeitsvermittlung_kompetenzbereiche"),
    url(r"^arbeitsvermittlung_ansprechpartner",TemplateView.as_view(template_name="web/pages/arbeitsvermittlung_ansprechpartner.html"),name="arbeitsvermittlung_ansprechpartner"),
    url(r"^arbeitsvermittlung",TemplateView.as_view(template_name="web/pages/arbeitsvermittlung.html"),name="arbeitsvermittlung"),
    url(r"^personalanfrage",TemplateView.as_view(template_name="web/pages/personalanfrage.html"),name="personalanfrage"),
    url(r"^personalauswahl",TemplateView.as_view(template_name="web/pages/personalauswahl.html"),name="personalauswahl"),
    url(r"^bewerber_zeitarbeit_vorteile",TemplateView.as_view(template_name="web/pages/bewerber_zeitarbeit_vorteile.html"),name="bewerber_zeitarbeit_vorteile"),
    url(r"^bewerber_zeitarbeit_berufsfelder",TemplateView.as_view(template_name="web/pages/bewerber_zeitarbeit_berufsfelder.html"),name="bewerber_zeitarbeit_berufsfelder"),
    url(r"^bewerber_zeitarbeit_ansprechpartner",TemplateView.as_view(template_name="web/pages/bewerber_zeitarbeit_ansprechpartner.html"),name="bewerber_zeitarbeit_ansprechpartner"),
    url(r"^bewerber_zeitarbeit",TemplateView.as_view(template_name="web/pages/bewerber_zeitarbeit.html"),name="bewerber_zeitarbeit"),
    url(r"^bewerber_personalvermittlung_vorteile",TemplateView.as_view(template_name="web/pages/bewerber_personalvermittlung_vorteile.html"),name="bewerber_personalvermittlung_vorteile"),
    url(r"^bewerber_personalvermittlung_berufsfelder",TemplateView.as_view(template_name="web/pages/bewerber_personalvermittlung_berufsfelder.html"),name="bewerber_personalvermittlung_berufsfelder"),
    url(r"^bewerber_personalvermittlung_ansprechpartner",TemplateView.as_view(template_name="web/pages/bewerber_personalvermittlung_ansprechpartner.html"),name="bewerber_personalvermittlung_ansprechpartner"),
    url(r"^bewerber_personalvermittlung",TemplateView.as_view(template_name="web/pages/bewerber_personalvermittlung.html"),name="bewerber_personalvermittlung"),
    url(r"^bewerber_arbeitsvermittlung_vorteile",TemplateView.as_view(template_name="web/pages/bewerber_arbeitsvermittlung_vorteile.html"),name="bewerber_arbeitsvermittlung_vorteile"),
    url(r"^bewerber_arbeitsvermittlung_berufsfelder",TemplateView.as_view(template_name="web/pages/bewerber_arbeitsvermittlung_berufsfelder.html"),name="bewerber_arbeitsvermittlung_berufsfelder"),
    url(r"^bewerber_arbeitsvermittlung_antworten",TemplateView.as_view(template_name="web/pages/bewerber_arbeitsvermittlung_antworten.html"),name="bewerber_arbeitsvermittlung_antworten"),
    url(r"^bewerber_arbeitsvermittlung_ansprechpartner",TemplateView.as_view(template_name="web/pages/bewerber_arbeitsvermittlung_ansprechpartner.html"),name="bewerber_arbeitsvermittlung_ansprechpartner"),
    url(r"^bewerber_arbeitsvermittlung",TemplateView.as_view(template_name="web/pages/bewerber_arbeitsvermittlung.html"),name="bewerber_arbeitsvermittlung"),
    url(r"^karriereberatung",TemplateView.as_view(template_name="web/pages/karriereberatung.html"),name="karriereberatung"),
    url(r"^karriere_activjob",TemplateView.as_view(template_name="web/pages/karriere_activjob.html"),name="karriere_activjob"),
    url(r"^zeitarbeit_kompetenzbereiche",TemplateView.as_view(template_name="web/pages/zeitarbeit_kompetenzbereiche.html"),name="zeitarbeit_kompetenzbereiche"),
    url(r"^zeitarbeit_ansprechpartner",TemplateView.as_view(template_name="web/pages/zeitarbeit_ansprechpartner.html"),name="zeitarbeit_ansprechpartner"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
