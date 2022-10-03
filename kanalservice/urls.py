from django.urls import path
from kanalservice.views import index

urlpatterns = [
    path("", index, name='index'),
]
