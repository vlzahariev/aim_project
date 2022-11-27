from django.contrib import admin

# from aimtravel_app.user_profile.forms import StudentEditForm

from aimtravel_app.user_profile.models import Students


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    # form = StudentEditForm
    list_display = ['first_name', 'last_name', 'bg_personal_number', 'university', 'user']
    list_filter = ['university']

