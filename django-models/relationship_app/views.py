from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.
def list_all_books(request):
    items = Book.objects.all()
    book_list = [f"{i.title} by {i.author}" for i in items]
    print(book_list)
    return render(request, "relationship_app/list_books.html", {"book_list": book_list})