from django.urls import path
from . import views


urlpatterns = [
    path('welcome', views.Front_page, name='hello'),
]
