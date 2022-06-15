from django.shortcuts import render

# Create your views here.


def studies_view(request):

    context = {

    }

    return render(request, 'studies/study.html', context)
