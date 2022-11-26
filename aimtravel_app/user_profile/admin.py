from django.contrib import admin
from django.contrib.auth import get_user_model

# from aimtravel_app.user_profile.forms import StudentEditForm

from aimtravel_app.user_profile.models import Students


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    # form = StudentEditForm
    pass
