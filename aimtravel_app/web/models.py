from django.db import models


class JobOffer(models.Model):
    state = models.CharField(
        max_length=20,
        blank=False,
        null=False,
    )

    city = models.CharField(
        max_length=20,
        blank=False,
        null=False,
    )

    job_position = models.CharField(
        max_length=30,
        blank=False,
        null=False,
    )

    employer = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    sponsor = models.CharField(
        max_length=15,
        blank=False,
        null=False,
    )

    wage = models.FloatField(
        blank=False,
        null=False,
    )
