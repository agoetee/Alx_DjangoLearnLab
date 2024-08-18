from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.
def list_all_books(request):
    items = Book.objects.all()
    book_list = [f"{i.title} by {i.author}" for i in items]
    return HttpResponse(f'{book_list}')