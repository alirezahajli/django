from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from decouple import config


class Command(BaseCommand):
    help = "Create super user"

    def handle(self, *args, **kwargs):
        User.objects.create_user(
            username=config("SUPER_USER_NAME"),
            email="",
            password=config("SUPER_USER_SECRET"),
        )
