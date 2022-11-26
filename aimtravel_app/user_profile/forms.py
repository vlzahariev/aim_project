from django import forms


from aimtravel_app.user_profile.models import Students

FAMILY_STATS_CHOICES = {
    ('single', 'Single'),
    ('Married', 'Married'),
    ('Other', 'Other'),
}
YES_NO_CHOICES = {
    ('yes', 'Yes'),
    ('no', 'No'),
}


class StudentEditForm(forms.ModelForm):
    family_status = forms.ChoiceField(choices=FAMILY_STATS_CHOICES,)
    is_received_visa = forms.BooleanField(required=False)
    is_fulltime_student = forms.BooleanField(required=False)
    date_of_birth = forms.DateField(
        required=False,
        input_formats=[
            '%d-%m-%y',
            '%d.%m.%y',
            '%Y-%m-%d',
            '%m/%d/%Y',
            '%m/%d/%y',
            '%b %d %Y',
            '%b %d, %Y',
            '%d %b %Y',
            '%d %b, %Y',
            '%B %d %Y',
            '%B %d, %Y',
            '%d %B %Y',
            '%d %B, %Y'],
        help_text='DD-MM-YYYY',
    )

    class Meta:
        model = Students
        exclude = ['user']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'middle_name': forms.TextInput(attrs={'placeholder': 'Middle Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'date_of_birth': forms.TextInput(attrs={'placeholder': 'Date of Birth'}),
            'place_of_birth': forms.TextInput(attrs={'placeholder': 'Place of Birth'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'province': forms.TextInput(attrs={'placeholder': 'Province'}),
            'street': forms.TextInput(attrs={'placeholder': 'Street'}),
            'family_status': forms.CharField(),
            'bg_personal_number': forms.TextInput(attrs={'placeholder': 'EGN'}),
            'nationality': forms.TextInput(attrs={'placeholder': 'Nationality'}),
            'country_of_birth': forms.TextInput(attrs={'placeholder': 'Country of Birth'}),
            'id_passport_number': forms.TextInput(attrs={'placeholder': 'Passport Number'}),
            'passport_date_of_issue': forms.TextInput(attrs={'placeholder': 'Passport Date of Issue'}),
            'is_received_visa': forms.BooleanField(),
            'Phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'university': forms.TextInput(attrs={'placeholder': 'University Name'}),
            'year_of_education': forms.TextInput(attrs={'placeholder': 'Year of Education'}),
            'foreign_university': forms.TextInput(attrs={'placeholder': 'Foreign University'}),
            'is_fulltime_student': forms.BooleanField(),
            'search_job_pref': forms.TextInput(attrs={'placeholder': 'Preferable job'}),
            'how_to_reach': forms.TextInput(attrs={'placeholder': 'How to reach you?'}),
        }


class StudentDetailsForm(forms.ModelForm):
    class Meta:
        model = Students
        exclude = ['user']