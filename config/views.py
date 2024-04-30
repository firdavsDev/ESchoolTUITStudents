from django.shortcuts import render

from events.models import Event
from cource.models import Course


def home(request):
    """A view that displays a main page."""
    events = Event.objects.filter(is_active=True).order_by('-created')[:3]
    courses = Course.objects.filter(is_active=True).order_by('-created')[:3]
    context = {
        'events': events,
        'courses': courses
    }
    return render(request, 'index.html', context)
