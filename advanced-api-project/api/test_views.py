from rest_framework import status
from django.test import APITestCase
from .models import Book, Author
from .seriealizers import BookSerializer

class BookCreateTest(APITestCase):
    def test_create_book(self):
        response = self.client.post("books/create")
        self.assertEqual(response.status_code, 200)

    def test_update_book(self):
        response = self.client.patch("books/update/<int:pk>")
        self.assertEqual(response.status_code, 200)

    def test_delete_book(self):
        response = self.client.post('books/delete/<int:pk>')
        self.assertEqual(response.status_code, 200)

        #Verify Book Creation
        # self.assertEqual(Book.objects.count(), 1)
        # self.assertEqual(book.title, data['title'])
        # self.assertEqual(book.author.name, self.author.name)
        # self.assertEqual(book.publication_year, data['publication_year'])