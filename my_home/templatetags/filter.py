import os.path

from django import template
from django.conf import settings

register = template.Library()


@register.filter()
def mediapath(image_path):
    media_url = settings.MEDIA_URL
    full_path = os.path.join(media_url, str(image_path))
    return full_path
