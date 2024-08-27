from django.urls import path
from .views import BookListAPIView

urlpatterns = [
    path('book_list/', BookListAPIView.as_view(), name='book_list')
]