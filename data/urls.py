from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt
from . import views

router = routers.DefaultRouter()
router.register('', views.current)
router.register('history', views.history_usd)
router.register('history-ratio', views.history_ratio)


app_name = "data"
urlpatterns = [
    path('v1/', include(router.urls)),
    path('token/', jwt.TokenObtainPairView.as_view(), name='token'),
	path('token-refresh/', jwt.TokenRefreshView.as_view(), name='refresh_token'),
]
