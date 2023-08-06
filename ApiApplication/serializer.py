from rest_framework import serializers


class BooksSerializer(serializers.Serializer):
    id = serializers.IntegerField(label = "Book ID")
    book_name = serializers.CharField(label= "Book Title")
    author = serializers.CharField(label = "Author Name")
    publisher = serializers.CharField(label = "Publisher Name")