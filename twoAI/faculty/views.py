from django.shortcuts import render
from .models import Faculty

# Create your views here.
def faculties(request):
    prof = Faculty.objects.all()
    return render(request, 'faculty/faculty.html', {'prof':prof})

