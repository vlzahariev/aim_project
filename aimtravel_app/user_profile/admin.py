from django.contrib import admin
from aimtravel_app.user_profile.models import Students, Employee


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'bg_personal_number', 'university', 'user']
    list_filter = ['university']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['user', 'employee_role', 'employee_first_name', 'employee_last_name']
    list_filter = ['employee_role']

