from django import template
from django.utils.timesince import timesince
from django.utils import timezone

register = template.Library()

@register.filter
def timesince_custom(value):
    now = timezone.now()

    try:
        difference = now - value
    except TypeError:
        return value

    if difference <= timezone.timedelta(minutes=1):
        return 'just now'
    elif difference <= timezone.timedelta(hours=1):
        return f'{difference.seconds // 60} minutes ago'
    elif difference <= timezone.timedelta(days=1):
        return f'{difference.seconds // 3600} hours ago'
    else:
        return timesince(value).split(', ')[0] + ' ago'
