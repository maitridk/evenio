"""
Views for evenio
"""
from evenio_cal.models import Event

from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object


def show_event(request, event_id):
    """ Show an event - wrapper arount object_detail 
        template: evenio/templates/event_detail.html
    """

    event = Event.objects.all()

    return object_detail(request, event, object_id=event_id, template_name="templates/evenio/event_detail.html")


def list_events(request):
    """ List events
        template: evenio/templates/event_list.html
    """

    events = Event.objects.all()

    return object_list(request, events, template_name="templates/event_list.html")


def create_event(request):
    """ Creates an event
        template: evenio/templates/event_form.html
    """

    return create_object(request, Event, template_name="templates/event_form.html")


def update_event(request, event_id):
    """ Updates an event
        template: evenio/templates/event_form.html
    """

    return update_object(request, Event, event_id, template_name="template/event_form.html")
