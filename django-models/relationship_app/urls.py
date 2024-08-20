from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from .views import list_books, LibraryDetailView, index
from . import views
from .views import librarian_view


urlpatterns = [
    path('books/', list_books, name='list_all_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_books'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('', index, name='index'),
    path('accounts/profile/', TemplateView.as_view(template_name='relationship_app/profile.html'), name='profile'),

    path('librarian_view/', librarian_view, name='librarian_view')
]