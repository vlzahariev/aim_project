from django.urls import path, include

from aimtravel_app.web import views
from aimtravel_app.web.views import CreateOfferView, DisplayOfferView, DisplayPriceView, AllEmployeeView, \
    DisplayAdditionalServicesView, EditOfferView, DeleteOfferView, DetailsOfferView

urlpatterns = (
    path('', views.index, name='index'),
    path('offer/', include([
        path('add/', CreateOfferView.as_view(), name='add offer'),
        path('offers/', DisplayOfferView.as_view(), name='offers'),
        path('edit/<int:pk>/', EditOfferView.as_view(), name='edit offer'),
        path('delete/<int:pk>/', DeleteOfferView.as_view(), name='delete offer'),
        path('details/<int:pk>/', DetailsOfferView.as_view(), name='details offer'),
    ])),
    path('prices/', DisplayPriceView.as_view(), name='prices'),
    path('services/', DisplayAdditionalServicesView.as_view(), name='show additional services'),
    path('company/', include([
        path('team/', AllEmployeeView.as_view(), name='team'),
    ])),
)
