from django import forms
from users.models import Role
from repairs.models import PlacesToWork, Repair, Status, TypeRepair
from django.contrib.auth import get_user_model


User = get_user_model()

class TechnicianForm(forms.ModelForm):
    """Форма для работы с заявкой для техника"""


    time_to_work = forms.DateTimeField(
        label="Дата выполнения",
        widget=forms.DateTimeInput(attrs={'class': 'form-control'})
    )
    places_to_work = forms.ModelChoiceField(
        label="Место выполнения",
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=PlacesToWork.objects.all()
    )
    type_repair = forms.ModelChoiceField(
        label="Тип поломки",
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=TypeRepair.objects.all()
    )

    status = forms.ChoiceField(
        label="Статус заявки",
        widget=forms.Select(
            attrs={'class': 'form-control'}
        ),
        choices=[
            item for item in Status.choices if item[0] in (
                'CONFIRMED', 'INCORRECT_DATA')
        ]
    )
    explanation = forms.CharField(
        label="Пояснения к заявке",
        widget=forms.Textarea(attrs={"class": "form-control", "style": "height: 50px; width: 100%;"})
    )
    users = forms.ModelMultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        queryset=User.objects.filter(role=Role.MASTER)
    )

    class Meta:
        model = Repair
        fields = (
            'time_to_work',
            'places_to_work',
            'type_repair',
            'status',
            'explanation',
            'users',
        )
