from django.shortcuts import render
from .models import Gallery, Announcement

def home(request):
    gallery = Gallery.objects.all()
    announcement = Announcement.objects.all()[:5]
    return render(request, 'home/home.html',{'gallery':gallery,'announcement':announcement})
    
