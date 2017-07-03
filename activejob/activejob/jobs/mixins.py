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

        self.q = session.get("jobs_q")
        if self.q:
            filter = (
                Q(title__icontains=self.q) |
                Q(location__icontains=self.q) |
                Q(description__icontains=self.q) |
                Q(profile__icontains=self.q) |
                Q(perspective__icontains=self.q) |

                Q(states__in=State.objects.filter(name__icontains=self.q))
            )

            queryset = queryset.filter(filter)

        self.states = session.get("jobs_states")
        if self.states:
            queryset = queryset.filter(states__in=[self.states])

        self.department = session.get("jobs_department")
        if self.department:
            queryset = queryset.filter(department=self.department)

        self.categories = session.get("jobs_categories")
        if self.categories:
            queryset = queryset.filter(categories__in=self.categories)

        return queryset

    def get_context_data(self):
        context = super().get_context_data()

        searchform = SearchForm(initial={
            "q": self.q,
            "categories": self.categories,
            "department": self.department,
            "states": self.states,
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
