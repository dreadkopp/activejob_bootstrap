from django import forms
from .models import Category, Department, State


class QuickSearchForm(forms.Form):
    q = forms.CharField(
        required=False,
        label="Stichwort",
    )


class SearchForm(QuickSearchForm):
    states = forms.ModelChoiceField(
        queryset=State.objects.exclude(job=None),
        empty_label="– alle Bundesländer –",
        required=False,
        widget=forms.Select(attrs={"onChange": "form.submit()"}),
        label="Bundesland",
    )

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.exclude(job=None),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Kategorie",
    )

    department = forms.ModelChoiceField(
        queryset=Department.objects.exclude(job=None),
        empty_label="– alle Bereiche –",
        required=False,
        widget=forms.Select(attrs={"onChange": "form.submit()"}),
        label="Bereich",
    )
