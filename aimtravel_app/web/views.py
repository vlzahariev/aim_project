from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.views.generic import DetailView

from aimtravel_app.user_profile.models import Students
from aimtravel_app.web.forms import JobOfferDetailForm
from aimtravel_app.web.models import JobOffer


# Create your views here.

def index(request):
    return render(request, template_name='index.html')


class CreateOfferView(views.CreateView):
    fields = '__all__'
    model = JobOffer
    template_name = 'job_offer/add_offer.html'
    success_url = reverse_lazy('index')


class DisplayOfferView(views.ListView):
    model = JobOffer
    template_name = 'job_offer/offers.html'
    context_object_name = 'offer_list'


