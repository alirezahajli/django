from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('', views.current)
router.register('history', views.history_usd)
router.register('history-ratio', views.history_ratio)


app_name = "data"
urlpatterns = [
    path('v1/', include(router.urls)),
]
