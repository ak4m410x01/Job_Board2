from django.urls import path
from . import views

urlpatterns = [
    path("", views.jobs),
    path("<int:id>", views.job_details),
]
