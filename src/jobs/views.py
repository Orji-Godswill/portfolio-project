from django.shortcuts import render
from . models import Job
# Create your views here.


def jobs_view(request):
    jobs = Job.objects.all()
    context = {
        'jobs': jobs
    }

    return render(request, 'jobs/jobs.html', context)
