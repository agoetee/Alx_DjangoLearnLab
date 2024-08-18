from django.urls import path
from .views import list_all_books, LibraryBooks

urlpatterns = [
    path('books/', list_all_books, name='list_all_books'),
    path('library/<int:pk>/', LibraryBooks.as_view(), name='library_books'),
]