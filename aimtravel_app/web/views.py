from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from aimtravel_app.web.models import JobOffer, Prices


# Create your views here.

def index(request):
    return render(request, template_name='index.html')


class CreateOfferView(LoginRequiredMixin, PermissionRequiredMixin, views.CreateView):
    permission_required = ('is_staff',)
    permission_denied_message = 'You don`t have required access.'
    fields = '__all__'
    model = JobOffer
    template_name = 'job_offer/add_offer.html'
    success_url = reverse_lazy('index1')


class DisplayOfferView(views.ListView):
    model = JobOffer
    template_name = 'job_offer/offers.html'
    context_object_name = 'offer_list'


class DisplayPriceView(views.ListView):
    model = Prices
    ordering = ['price']
    template_name = 'price/prices.html'
    context_object_name = 'prices_list'



