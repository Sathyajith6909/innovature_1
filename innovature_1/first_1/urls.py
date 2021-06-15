from django.urls import path
from . import views


urlpatterns = [
    path('welcome', views.books_list, name='hello'),
]
