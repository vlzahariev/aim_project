from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView, ListView

from aimtravel_app.user_profile.forms import StudentEditForm, StudentDetailsForm, EmployeeDetailsForm
from aimtravel_app.user_profile.models import Students, Employee


# Create your views here.
class EditUserProfileView(LoginRequiredMixin, UpdateView):
    model = Students
    form_class = StudentEditForm
    template_name = 'user_profile/edit_personal_profile.html'

    def get_success_url(self):
        student_pk = self.kwargs['pk']
        return reverse_lazy('details profile', kwargs={'pk': student_pk})


class UserProfileView(LoginRequiredMixin, DetailView):
    model = Students
    template_name = 'user_profile/personal_profile.html'
    form_class = StudentDetailsForm


class EmployeeProfileView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Employee
    permission_required = 'is_staff'
    template_name = 'user_profile/employee_profile.html'
    form_class = EmployeeDetailsForm


class AllEmployeeView(ListView):
    model = Employee
    template_name = 'about_us/team.html'
    context_object_name = 'employee_list'
