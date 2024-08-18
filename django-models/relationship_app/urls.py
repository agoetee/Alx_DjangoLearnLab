from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import list_books, LibraryDetailView, register, LoginView, index

urlpatterns = [
    path('books/', list_books, name='list_all_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_books'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(next_page='books')),
    path('logout/', LogoutView.as_view(next_page='/')),
    path('', index, name='index'),
]