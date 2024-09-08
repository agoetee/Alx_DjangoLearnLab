from django.urls import path
from .views import CustomBookCreateView, CustomBookListView, CustomBookDetailView, CustomBookUpdateView, CustomBookDeleteView

urlpatterns = [
    path('books/', CustomBookListView.as_view(), name='list'),
    path('book/<int:pk>', CustomBookDetailView.as_view(), name='detail'),
    path('book/update/<int:pk>', CustomBookUpdateView.as_view(), name='update'),
    path('book/delete/<int:pk>', CustomBookDeleteView.as_view(), name='delete'),
    path('book/create', CustomBookCreateView.as_view(), name='create'),
]