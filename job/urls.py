from django.urls import path
from . import views

app_name = "jobs"

urlpatterns = [
    path("", views.jobs, name="jobs_list"),
    path("<int:id>", views.job_details, name="job_details"),
]
