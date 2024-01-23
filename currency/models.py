from django.db import models

class ExchangeRateRequest(models.Model):
    request_time = models.DateTimeField(auto_now_add=True)
    usd_to_rub_rate = models.FloatField()
