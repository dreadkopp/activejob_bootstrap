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
from django.core.paginator import Paginator



class MenuItem:
    def __init__(self, name, url, active=False, sublist=None):
        self.name = name
        self.url = url
        self.active = active
        self.sublist = sublist

class ContactPerson:
    def __init__(self, name, stat, phone, mail, imageurl):
        self.name = name
        self.stat = stat
        self.phone = phone
        self.mail = mail
        self.imageurl = imageurl

class Location:
    def __init__(self, name, street, city, phone, fax, mail, gmapsIframeHref ):
        self.name = name
        self.street = street
        self.city = city
        self.phone = phone
        self.fax = fax
        self.mail = mail
        self.gmapsIframeHref = gmapsIframeHref

class Job:
    def __init__(self, name, slug, location):
        self.name = name
        self.slug = slug
        self.location = location
    def __str__(self):
        return self.name

def generate_jobs(count):
    jobs = []
    for i in range(count):
        jobs.append(Job("Beschaeftigungstherapie","somewhere.com","somewhere"))
    return jobs

"""testcase no pagination, only for the looks"""
jobs = generate_jobs(100);
paginator = Paginator(jobs,10);
page_obj = paginator.page(1);


standorte = [
    Location("Standort Springfield", "742 Evergreen Terrace", "<somezipcode> Springfield", "555-SIMPSONS", "555-SIMPSONSFAX", "simpsons@somewhere.com", "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3224.6601807984257!2d-115.01758844877891!3d36.07739181565208!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80c8d0b899a5328b%3A0x53a02fbbc05432c3!2s712+Red+Bark+Ln%2C+Henderson%2C+NV+89011%2C+USA!5e0!3m2!1sde!2sde!4v1494937738392" ),
    Location("Standort Springfield", "742 Evergreen Terrace", "<somezipcode> Springfield", "555-SIMPSONS", "555-SIMPSONSFAX", "simpsons@somewhere.com", "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3224.6601807984257!2d-115.01758844877891!3d36.07739181565208!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80c8d0b899a5328b%3A0x53a02fbbc05432c3!2s712+Red+Bark+Ln%2C+Henderson%2C+NV+89011%2C+USA!5e0!3m2!1sde!2sde!4v1494937738392" ),
]

menu_left = [
    MenuItem("Ipsum","#",active=True,sublist=[
        MenuItem("Lorem","#"),
        MenuItem("Larum","#",active=True),
    ]),
    MenuItem("Lorem","#"),
    MenuItem("Larum","#"),
]
menu_top = [
    MenuItem("Home","/",active=True),
    MenuItem("Ueber Uns","#"),
    MenuItem("Unternehmen","#"),
    MenuItem("Bewerber","#"),
]

ansprechpartner = [
    ContactPerson("John Doe","Platzhalter","555-424242","JohnDoe@Platzhalter.de","res/Ansprechpartner/JohnDoe.png"),
    ContactPerson("John Doe","Platzhalter","555-424242","JohnDoe@Platzhalter.de","res/Ansprechpartner/JohnDoe.png"),
    ContactPerson("John Doe","Platzhalter","555-424242","JohnDoe@Platzhalter.de","res/Ansprechpartner/JohnDoe.png"),
    ContactPerson("John Doe","Platzhalter","555-424242","JohnDoe@Platzhalter.de","res/Ansprechpartner/JohnDoe.png"),
]

class ActivJobView(TemplateView):
    menu_left = []
    menu_top = []
    ansprechpartner = []
    standorte = []
    page_obj = []
    def set_activeJob_context(self, menu_left=[], menu_top=[], ansprechpartner=[], standorte=[], page_obj=[]):
        self.menu_left = menu_left
        self.menu_top = menu_top
        self.ansprechpartner = ansprechpartner
        self.standorte = standorte
        self.page_obj = page_obj

    def get_context_data(self, **kwargs):
        context = super(MyTemplateView, self).get_context_data(**kwargs)
        context.update({"menu_left": self.menu_left})
        context.update({"menu_top": self.menu_top})
        context.update({"ansprechpartner": self.ansprechpartner})
        context.update({"standorte": self.standorte})
        context.update({"page_obj": self.page_obj})
        return context

def testview():
    view = ActivJobView()
    view.set_activeJob_context(menu_left,menu_top,ansprechpartner,standorte,page_obj)
    return view.as_view(template_name="test/test.html")

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
    url(r'^test', testview()),
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
    view(r'^bewerber_personalvermittlung_vorteile'),
    view(r'^bewerber_personalvermittlung_berufsfelder'),
    view(r'^bewerber_personalvermittlung_ansprechpartner'),
    view(r'^bewerber_personalvermittlung'),
    view(r'^bewerber_zeitarbeit_vorteile'),
    view(r'^bewerber_zeitarbeit_berufsfelder'),
    view(r'^bewerber_zeitarbeit_ansprechpartner'),
    view(r'^bewerber_zeitarbeit'),
    view(r'^bewerber'),
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
