from __future__ import unicode_literals

from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from django.conf import settings
from django.contrib.auth.decorators import login_required

from resources.utils import get_resource_stats

DEFAULT_HITS = 50000


def index(request):
    data = cache.get('resource_data')
    if not data:
        data = get_resource_stats()
        cache.set('resource_data', data, 10000)
    return render_to_response(
        'index.html',
        data
    )


def documentation(request):
    return render_to_response("documentation.html")

