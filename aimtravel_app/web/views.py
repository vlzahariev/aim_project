from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from aimtravel_app.user_profile.models import Employee
from aimtravel_app.web.forms import JobOfferDetailForm, JobOfferEditForm
from aimtravel_app.web.models import JobOffer, Prices, AdditionalServices


# Create your views here.

def index(request):
    return render(request, template_name='index.html')


class CreateOfferView(LoginRequiredMixin, PermissionRequiredMixin, views.CreateView):
    permission_required = ('is_staff',)
    permission_denied_message = 'Нямаш необходимите права.'
    fields = '__all__'
    model = JobOffer
    template_name = 'job_offer/add_offer.html'
    success_url = reverse_lazy('index')


class DisplayOfferView(views.ListView):
    model = JobOffer
    template_name = 'job_offer/offers.html'
    context_object_name = 'offer_list'


class DetailsOfferView(views.DetailView):
    model = JobOffer
    template_name = 'job_offer/details_offer.html'
    form_class = JobOfferDetailForm
    context_object_name = 'offer_details'


class EditOfferView(LoginRequiredMixin, PermissionRequiredMixin, views.UpdateView):
    model = JobOffer
    fields = '__all__'
    permission_required = ('is_staff',)
    permission_denied_message = 'Нямаш необходимите права.'
    template_name = 'job_offer/edit_offer.html'
    context_object_name = 'edit_offer'

    def get_success_url(self):
        offer_pk = self.kwargs['pk']
        return reverse_lazy('details offer', kwargs={'pk': offer_pk})


class DeleteOfferView(LoginRequiredMixin, PermissionRequiredMixin, views.DeleteView):
    model = JobOffer
    permission_required = ('is_staff',)
    permission_denied_message = 'Нямаш необходимите права.'
    template_name = 'job_offer/delete_offer.html'
    context_object_name = 'delete_offer'
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('offers')


class DisplayPriceView(views.ListView):
    model = Prices
    ordering = ['price']
    template_name = 'price/prices.html'
    context_object_name = 'prices_list'


class DisplayAdditionalServicesView(views.ListView):
    model = AdditionalServices
    template_name = 'additional_services/additional_services.html'
    context_object_name = 'services_list'


class AllEmployeeView(views.ListView):
    model = Employee
    template_name = 'about_us/team.html'
    context_object_name = 'employee_list'
