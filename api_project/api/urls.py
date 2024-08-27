from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet, basename='books' )

urlpatterns = [
    path('books/list/', BookViewSet.as_view({'get': 'list_books'}), name='list_books'),
    path('books/create', BookViewSet.as_view({'post': 'create_book'}), name='create_book')
    # path('', include(router.urls))
]

urlpatterns += router.urls