from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as CustomUserAdmin

from .models import Book, User

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ['title']

admin.site.register(Book, BookAdmin)


class UserAdmin(CustomUserAdmin):
    pass

admin.site.register(User, UserAdmin)
