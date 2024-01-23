from django.http import JsonResponse
from .models import ExchangeRateRequest
import requests
from datetime import datetime, timedelta


def get_exchange_rate():
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    data = response.json()
    return data['rates']['RUB']


def get_current_usd(request):
    now = datetime.now()
    recent_requests = ExchangeRateRequest.objects.filter(request_time__gte=now - timedelta(seconds=10))

    if not recent_requests.exists():
        rate = get_exchange_rate()
        ExchangeRateRequest.objects.create(usd_to_rub_rate=rate)
    else:
        rate = recent_requests.first().usd_to_rub_rate

    last_10_requests = ExchangeRateRequest.objects.order_by('-request_time')[:10]
    rates_history = [{'request_time': req.request_time, 'rate': req.usd_to_rub_rate} for req in last_10_requests]

    return JsonResponse({'current_rate': rate, 'last_10_requests': rates_history})





