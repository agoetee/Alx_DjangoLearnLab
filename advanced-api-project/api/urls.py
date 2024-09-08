from django.urls import path
from .views import CustomBookCreateView, CustomBookListView, CustomBookDetailView, CustomBookUpdateView, CustomBookDeleteView

urlpatterns = [
    path('books/', CustomBookListView.as_view(), name='list'),
    path('book/<int:pk>', CustomBookDetailView.as_view(), name='detail'),
    path('book/<int:pk>', CustomBookUpdateView.as_view(), name='update'),
    path('book/<int:pk>', CustomBookDeleteView.as_view(), name='delete'),
    path('book/', CustomBookCreateView.as_view(), name='create'),
]