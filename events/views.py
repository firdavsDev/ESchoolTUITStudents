from django.shortcuts import render

from .models import Event


def event_list(request):
    events = Event.objects.filter(is_active=True)
    return render(request, 'events/list.html', {'events': events})


def event_detail(request, pk):
    event = Event.objects.get(pk=pk, is_active=True)
    return render(request, 'events/detail.html', {'event': event})
