from django.shortcuts import render, redirect
from jobs.models import Job


def index_view(request):
    job_obj = Job.objects.all()
    context = {
        'job_obj': job_obj
    }
    return render(request, 'index.html', context)


def contact_view(request):
    return render(request, 'base/contact.html')
