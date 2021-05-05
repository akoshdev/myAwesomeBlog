from django.shortcuts import render
from .models import Event  # EVENT lesson

# Create your views here.
events = Event.objects       # EVENT lesson
def home(request):
    return render(request,'events/home.html', {'events': events})