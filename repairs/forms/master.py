from django import forms
from repairs.models import Parts, Repair, Status, works


class MasterForm(forms.ModelForm):
    """Форма для мастера"""

    parts = forms.ModelMultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        queryset=Parts.objects.all(),
    )
    status = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=[
            item for item in Status.choices if item[0] in (
                'READY_TO_WORK', 'RE_REPAIR', 'VERIFICATION'
            )
        ]
    )


    class Meta:
        model = Repair
        fields = (
            'parts',
            'status',
        )
