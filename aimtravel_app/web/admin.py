from django.contrib import admin

from aimtravel_app.web.models import JobOffer


# Register your models here.
@admin.register(JobOffer)
class JobOfferAdmin(admin.ModelAdmin):
    pass
