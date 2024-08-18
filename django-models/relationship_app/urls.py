from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import list_books, LibraryDetailView, LoginView, index
from . import views

urlpatterns = [
    path('books/', list_books, name='list_all_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_books'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html')),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html')),
    path('', index, name='index'),
]