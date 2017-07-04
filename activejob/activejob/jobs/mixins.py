from django.db.models import Q

from .models import Category, State
from .forms import QuickSearchForm, SearchForm


class SearchMixin:
    def get_queryset(self):
        request = self.request
        session = request.session

        if "jobs_categories" not in session:
            session["jobs_categories"] = [
                category.id for category in Category.objects.all()
            ]

        if "q" in request.GET:
            session["jobs_q"] = request.GET.get("q")
            session["jobs_states"] = request.GET.get("states")
            session["jobs_department"] = request.GET.get("department")

            session["jobs_categories"] = request.GET.getlist("categories") \
                or [category.id for category in Category.objects.all()]

        queryset = super().get_queryset().distinct()

        for word in session.get("jobs_q").split():
            filter = (
                Q(title__icontains=word) |
                Q(location__icontains=word) |
                Q(description__icontains=word) |
                Q(profile__icontains=word) |
                Q(perspective__icontains=word) |

                Q(states__in=State.objects.filter(name__icontains=word))
            )

            queryset = queryset.filter(filter)

        if session.get("jobs_states"):
            queryset = queryset.filter(states__in=[session.get("jobs_states")])

        if session.get("jobs_department"):
            queryset = queryset.filter(department=session.get("jobs_department"))

        if session.get("jobs_categories"):
            queryset = queryset.filter(categories__in=session.get("jobs_categories"))

        return queryset

    def get_context_data(self):
        context = super().get_context_data()

        session = self.request.session
        searchform = SearchForm(initial={
            "q": session.get("jobs_q"),
            "categories": session.get("jobs_categories"),
            "department": session.get("jobs_department"),
            "states": session.get("jobs_states"),
        })

        context.update({
            "searchform": searchform,
        })

        return context


class QuickSearchFormMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quicksearchform = QuickSearchForm()
        context.update({"quicksearchform": quicksearchform})
        return context
