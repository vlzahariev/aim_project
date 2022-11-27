from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from model_utils import Choices


from aimtravel_app import settings
from aimtravel_app.user_auth.models import AppUser

UserModel = get_user_model()


# Create your models here.

class Students(models.Model):
    FAMILY_STATUS = Choices('Single', 'Married', 'Engaged',)

    user = models.OneToOneField(
        UserModel,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    first_name = models.CharField(
        max_length=15,
        verbose_name='First name',
        help_text='Please enter your given name',
        blank=True,
        null=True,
        default='',
    )
    middle_name = models.CharField(
        max_length=15,
        verbose_name='Middle name',
        help_text='Please enter your middle name',
        blank=True,
        null=True,
        default='',
    )
    last_name = models.CharField(
        max_length=15,
        verbose_name='Last name',
        help_text='Please enter your last name',
        blank=True,
        null=True,
        default='',
    )
    date_of_birth = models.DateField(
        verbose_name='Date of birth',
        help_text='dd-mm-yyyy',
        blank=True,
        null=True,
    )
    place_of_birth = models.CharField(
        max_length=15,
        help_text='Citi where you were born',
        blank=True,
        null=True,
        default='',
    )
    city = models.CharField(
        max_length=15,
        help_text='Please choose',
        blank=True,
        null=True,
        default='',
    )
    province = models.CharField(
        max_length=15,
        help_text='Please choose',
        blank=True,
        null=True,
        default='',
    )
    street = models.CharField(
        max_length=30,
        help_text='Please choose',
        blank=True,
        null=True,
        default='',
    )
    family_status = models.CharField(
        max_length=8,
        default='Single',
        choices=FAMILY_STATUS,

    )
    bg_personal_number = models.CharField(
        max_length=15,
        verbose_name='EGN',
        help_text='EGN',
        blank=True,
        null=True,
        default='',
    )
    nationality = models.CharField(
        max_length=15,
        help_text='Your nationality',
        blank=True,
        null=True,
        default='',
    )
    country_of_birth = models.CharField(
        max_length=15,
        help_text='Which country you were born',
        blank=True,
        null=True,
        default='',
    )

    id_passport_number = models.CharField(
        max_length=15,
        help_text='Document number',
        blank=True,
        null=True,
        default='',
    )
    passport_date_of_issue = models.DateField(
        blank=True,
        null=True,
    )
    is_received_visa = models.BooleanField(
        blank=True,
        null=True,
    )
    phone = models.CharField(
        max_length=15,
        help_text='Your phone number',
        blank=True,
        null=True,
        default='',
    )
    email = models.CharField(
        max_length=40,
        blank=True,
        null=True,
        default='',
    )
    university = models.CharField(
        max_length=30,
        help_text='Your university',
        blank=True,
        null=True,
        default='',
    )
    year_of_education = models.PositiveIntegerField(
        help_text='Курс',
        blank=True,
        null=True,
    )
    foreign_university = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        default='',
    )
    is_fulltime_student = models.BooleanField(
        blank=True,
        null=True,
    )
    search_job_pref = models.CharField(
        default='',
        max_length=15,
        blank=True,
        null=True,
    )
    how_to_reach = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        default='',
    )

    def __str__(self):
        name_str = f"{self.user}\n"
        if self.first_name:
            name_str += '\n' + '-' + '\n' + self.first_name
        if self.last_name:
            name_str += '\n' + self.last_name
        return name_str

    @receiver(post_save, sender=UserModel)
    def create_profile(sender, instance, created, *args, **kwargs):
        if created:
            Students.objects.create(user=instance)
