from django import forms
from django.utils.translation import gettext as _


SEARCH_TYPE_CHOICES = (
    ('rooms', _("Habitaciones")),
    ('sale', _("Venta")),
    ('rent', _("Alquiler")),
)


class SearchForm(forms.Form):
    search_type = forms.ChoiceField(
        label=_("Tipo de búsqueda"),
        choices=SEARCH_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'custom-select'}),
    )
    address = forms.CharField(
        label=_("Dirección"),
        max_length=500,
        widget=forms.TextInput(attrs={'class': 'custom-textinput'})
    )
    latitude = forms.FloatField(required=False, widget=forms.HiddenInput)
    longitude = forms.FloatField(required=False, widget=forms.HiddenInput)
