from django.shortcuts import render
from .models import Job
from .forms import ApplyForm
from django.core.paginator import Paginator

# Create your views here.


def jobs(request):
    jobs_all = Job.objects.all()

    paginator = Paginator(jobs_all, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"jobs": page_obj}
    return render(request, "job/jobs.html", context)


def job_details(request, slug):
    job = Job.objects.get(slug=slug)
    if request.method == "POST":
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job
            myform.save()
    else:
        form = ApplyForm()

    context = {
        "job": job,
        "form": form,
    }
    return render(request, "job/job_details.html", context)
