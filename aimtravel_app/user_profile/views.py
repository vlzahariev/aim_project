from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView

from aimtravel_app.user_profile.forms import StudentEditForm, StudentDetailsForm
from aimtravel_app.user_profile.models import Students


# Create your views here.
class EditUserProfileView(UpdateView):
    model = Students
    form_class = StudentEditForm
    template_name = 'user_profile/edit_personal_profile.html'

    def get_success_url(self):
        student_pk = self.kwargs['pk']
        return reverse_lazy('details profile', kwargs={'pk': student_pk})


class UserProfileView(DetailView):
    model = Students
    template_name = 'user_profile/personal_profile.html'
    form_class = StudentDetailsForm
