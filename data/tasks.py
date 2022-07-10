from datetime import timedelta

from .crawl import GetData
from .models import CurrenciesData

from celery import shared_task
from django_celery_beat.models import PeriodicTask
from django.utils import timezone


@shared_task
def currency_fetcher():

    last_usd_amount = GetData().get_last_amount("usd")
    last_euro_amount = GetData().get_last_amount("euro")

    ratio = float(last_usd_amount / last_euro_amount)
    CurrenciesData.objects.create(
        currency="usd", amount=last_usd_amount, ratio_of_dollar_on_euro=ratio
    )
    CurrenciesData.objects.create(
        currency="euro", amount=last_euro_amount, ratio_of_dollar_on_euro=ratio
    )


@shared_task
def time_scheduler():
    if (
        timedelta(hours=5, minutes=30)
        < timedelta(hours=timezone.now().hour, minutes=timezone.now().minute)
        < timedelta(hours=13, minutes=30)
    ):

        task = PeriodicTask.objects.get(name="currency fetcher")
        task.enabled = True
        task.save()
    else:

        task = PeriodicTask.objects.get(name="currency fetcher")
        task.enabled = False
        task.save()
