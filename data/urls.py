from django.urls import path
from . import views


app_name = "data"
urlpatterns = [
    path("", views.home, name="data"),
    path("current/usd", views.current_usd),
    path("current/euro", views.current_euro),
    path("history/usd", views.history_usd),
    path("history/euro", views.history_euro),
    path("history/ratio", views.history_ratio),
]
