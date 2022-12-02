from django import forms

from aimtravel_app.web.models import JobOffer


class JobOfferDetailForm(forms.ModelForm):
    class Meta:
        model = JobOffer
        fields = '__all__'


class JobOfferEditForm(forms.ModelForm):
    class Meta:
        model = JobOffer
        fields = '__all__'

        widgets = {
            'job_position': forms.TextInput(attrs={'placeholder': 'Позиция'}),
            'employer': forms.TextInput(attrs={'placeholder': 'Работодател'}),
            'city': forms.TextInput(attrs={'placeholder': 'Град'}),
            'state': forms.TextInput(attrs={'placeholder': 'Щат'}),
            'sponsor': forms.TextInput(attrs={'placeholder': 'Спонсор'}),
            'offer_pic': forms.TextInput(attrs={'placeholder': 'Снимка-URL'}),
        }
