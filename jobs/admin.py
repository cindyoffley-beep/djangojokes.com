from django.contrib import admin

from .models import Job, Applicant


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "updated")


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "job",
        "created",
    )