from django import forms
from repairs.models import Repair, PlacesToWork, Comp


class CustomerForm(forms.ModelForm):
    description = forms.CharField(
        label="Описание поломки",
        widget=forms.Textarea(attrs={"class": "form-control", "style": "height: 100px; width: 100%;"})
    )
    places_to_work = forms.ModelChoiceField(
        label="Площадка",
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=PlacesToWork.objects.all()
    )

    class Meta:
        model = Repair
        fields = ('description', 'places_to_work', 'idcomp')
