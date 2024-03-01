from __future__ import unicode_literals

from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from django.conf import settings
from django.contrib.auth.decorators import login_required

import stripe

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


@csrf_exempt
def stripe_donation(request):
    if request.method == 'POST':
        # Amount in cents
        amount = 1000

        stripe.api_key = settings.STRIPE_KEYS['secret']

        customer = stripe.Customer.create(
            email=request.POST.get('stripeEmail', ''),
            card=request.POST.get('stripeToken', '')
        )

        try:
            stripe.Charge.create(
                customer=customer.id,
                amount=amount,
                currency='usd',
                description='SWAPI donation'
            )
        except:
            pass

        return redirect('/')
    return redirect('/')


@login_required
def stats(request):
    data = {}
    data['keen_project_id'] = settings.KEEN_PROJECT_ID
    data['keen_read_key'] = settings.KEEN_READ_KEY
    return render_to_response(
        'stats.html',
        data
    )
