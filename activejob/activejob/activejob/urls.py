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
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.conf.urls.static import static
from django.conf import settings

siteTemplatesRootDir = 'web/pages/'

"""spare some typing"""
def view(regex):
    str = regex[1:]
    str =  siteTemplatesRootDir + str + '.html'
    if regex == r'^$':
        return url(regex, TemplateView.as_view(template_name="web/pages/home.html"))
    else:
        return url(regex, TemplateView.as_view(template_name=str))


urlpatterns = [
    view(r'^$'),
    view(r'^arbeitnehmerueberlassung'),
    view(r'^arbeitsvermittlung_kompetenzbereiche'),
    view(r'^arbeitsvermittlung_ansprechpartner'),
    view(r'^arbeitsvermittlung'),
    view(r'^bewerber_arbeitsvermittlung_vorteile'),
    view(r'^bewerber_arbeitsvermittlung_berufsfelder'),
    view(r'^bewerber_arbeitsvermittlung_antworten'),
    view(r'^bewerber_arbeitsvermittlung_ansprechpartner'),
    view(r'^bewerber_arbeitsvermittlung'),
    view(r'^bewerber'),
    view(r'^bewerber_personalvermittlung_vorteile'),
    view(r'^bewerber_personalvermittlung_berufsfelder'),
    view(r'^bewerber_personalvermittlung_ansprechpartner'),
    view(r'^bewerber_personalvermittlung'),
    view(r'^bewerber_zeitarbeit_vorteile'),
    view(r'^bewerber_zeitarbeit_berufsfelder'),
    view(r'^bewerber_zeitarbeit_ansprechpartner'),
    view(r'^bewerber_zeitarbeit'),
    view(r'^home'),
    view(r'^impressum'),
    view(r'^karriere_activjob'),
    view(r'^karriereberatung'),
    view(r'^kontakt'),
    view(r'^leitbild'),
    view(r'^personalauswahl'),
    view(r'^personalanfrage'),
    view(r'^personalvermittlung_referenzen'),
    view(r'^personalvermittlung_kompetenzbereiche'),
    view(r'^personalvermittlung_ansprechpartner'),
    view(r'^personalvermittlung'),
    view(r'^sitemap'),
    view(r'^standorte'),
    view(r'^standort'),
    view(r'^stellenmarkt'),
    view(r'^unternehmensprofil'),
    view(r'^unternehmen'),
    view(r'^zeitarbeit_kompetenzbereiche'),
    view(r'^zeitarbeit_ansprechpartner'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
