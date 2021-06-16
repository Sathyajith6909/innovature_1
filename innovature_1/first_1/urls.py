from django.urls import path
from . import views
# from .views import BookDetailAV
from .views import ShelfList


urlpatterns = [
    # path('stream_apiv/<int:pk>', views.books_list, name='hello'),
    # path('stream/<int:pk>', BookDetailAV.as_view(), name="streamplatform-detail"),
    path('stream_generics/<int:pk>', ShelfList.as_view(), name="streamplatform"),
]
