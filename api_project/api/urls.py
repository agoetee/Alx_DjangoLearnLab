from django.urls import path
from .views import BookListCreateAPIView

urlpatterns = [
    path('book_list/', BookListCreateAPIView.as_view(), name='book_list')
]