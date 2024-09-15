from django.urls import path
from .views import LoginView, register, LogoutView, profile, edit_profile, CreateView, UpdateView, DetailView, DeleteView, ListView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile' ),
    path('posts/new/', CreateView.as_view(), name='new'),
    path('posts/', ListView.as_view(), name='posts'),
    path('posts/<int:pk>', DetailView.as_view(), name='detail'),
    path('posts/<int:pk>/delete', DeleteView.as_view(), name='delete'),
    path('posts/<int:pk>/edit', UpdateView.as_view(), name='update'),

]