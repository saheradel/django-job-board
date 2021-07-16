from django.shortcuts import render
from .models import Job


def job_list(request):
    all_jobs = Job.objects.all()
    context = {'jobs' : all_jobs}
    return render(request, 'job/job_list.html', context)


def job_detail(request, id):
    job_detail = Job.objects.get(id=id)
    context = {'job': job_detail}
    return render(request, 'job/job_detail.html', context)
