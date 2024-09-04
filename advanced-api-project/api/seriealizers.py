from rest_framework import serializers
from .models import Book, Author
import datetime

class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)

chima = Author(name='Chimmamanda Ngozie')

class BookSerializer(serializers.Serializer):
    title = serializers.CharField()
    publication_year = serializers.IntegerField(validate_year)
    author = AuthorSerializer()

    def validate_year(self, data):
        current_year = datetime.date.today().year
        if data['publication_year'] > current_year:
            raise serializers.validationError(f'Publication year cannot be greater than current year: {current_year}')
        return data


purple= Book(title="Purple Hibiscus", publication_year='2020', author=chima)

