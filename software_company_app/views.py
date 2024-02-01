from django.shortcuts import render
from .models import Error, Programmer, ErrorCorrection

def project_info(request):
    errors = Error.objects.all()
    programmers = Programmer.objects.all()
    error_corrections = ErrorCorrection.objects.all()

    return render(request, 'software_company_app/project_info.html', {'errors': errors, 'programmers': programmers, 'corrections': error_corrections})