from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator

# Create your views here.


def jobs(request):
    jobs_all = Job.objects.all()

    paginator = Paginator(jobs_all, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {"jobs": page_obj}
    return render(request, "job/jobs.html", context)


def job_details(request, id):
    job = Job.objects.get(id=id)
    context = {"job": job}
    return render(request, "job/job_details.html", context)
