from django.urls import path
from .views import LoginView, register, LogoutView, profile, edit_profile, CreateView, UpdateView, DetailView, DeleteView, ListView
from .views import CommentCreateView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile' ),
    path('post/new/', CreateView.as_view(), name='new'),
    path('posts/', ListView.as_view(), name='posts'),
    path('post/<int:pk>', DetailView.as_view(), name='detail'),
    path('post/<int:pk>/delete/', DeleteView.as_view(), name='delete'),
    path('post/<int:pk>/update/', UpdateView.as_view(), name='update'),
    path('post/<int:pk>/comment/new/', CommentCreateView.as_view(), name='new_comment')

]