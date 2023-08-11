from django.shortcuts import render
from .models import Job

# Create your views here.


def jobs(request):
    jobs_all = Job.objects.all()
    context = {"jobs": jobs_all}
    return render(request, "job/jobs.html", context)


def job_details(request, id):
    job = Job.objects.get(id=id)
    context = {"job": job}
    return render(request, "job/job_details.html", context)
