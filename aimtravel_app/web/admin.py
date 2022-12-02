from django.contrib import admin

from aimtravel_app.web.models import JobOffer, Prices, AdditionalServices


# Register your models here.
@admin.register(JobOffer)
class JobOfferAdmin(admin.ModelAdmin):
    pass


@admin.register(Prices)
class PricesAdmin(admin.ModelAdmin):
    pass


@admin.register((AdditionalServices))
class AdditionalServicesAdmin(admin.ModelAdmin):
    pass
