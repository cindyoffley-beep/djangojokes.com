from django.db import models
from django.core.validators import URLValidator


class Job(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Applicant(models.Model):
    EMPLOYMENT_TYPES = (
        ("full-time", "Full-time"),
        ("part-time", "Part-time"),
        ("contract", "Contract work"),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    website = models.URLField(
        blank=True,
        validators=[URLValidator()]
    )

    employment_type = models.CharField(
        max_length=20,
        choices=EMPLOYMENT_TYPES
    )

    start_date = models.DateField(
        help_text="The earliest date you can start working."
    )

    available_days = models.CharField(
        max_length=100,
        help_text="Select all days that you can work."
    )

    desired_hourly_wage = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    cover_letter = models.TextField()
    confirmation = models.BooleanField()

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.job}"