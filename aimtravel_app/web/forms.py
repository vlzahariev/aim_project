from django import forms

from aimtravel_app.web.models import JobOffer


class JobOfferDetailForm(forms.ModelForm):
    class Meta:
        model = JobOffer
        fields = '__all__'
