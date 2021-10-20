from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.authtoken.views import obtain_auth_token
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("data.urls", namespace="data")),
    path("api-token-auth/", obtain_auth_token),
    path("api-auth/", include("rest_framework.urls")),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
