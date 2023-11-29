from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    author_books_count = serializers.SerializerMethodField()

    def get_author_books_count(self, instance):
        return Book.objects.filter(author=instance.author).count()

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author',
            'publication_year',
            'isbn',
            'author_books_count'
        ]
