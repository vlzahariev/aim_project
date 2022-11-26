from django.urls import path

from aimtravel_app.web import views
from aimtravel_app.web.views import CreateOfferView, DisplayOfferView

urlpatterns = (
    path('', views.index, name='index'),
    path('add_offer/', CreateOfferView.as_view(), name='add offer'),
    path('offers/', DisplayOfferView.as_view(), name='offers'),
)
