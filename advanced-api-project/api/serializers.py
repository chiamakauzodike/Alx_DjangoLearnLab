from rest_framework import serializers
from .models import Book
from .models import Author
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fileds = '__all__'

    def validate_publication_date(self, value)
        if value > date.today():
            raise serializers.ValidationError("Publication date must not be in the future")
        return value
    
class AuthorSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Authorfields = ['name', 'date_of_birth', 'bio', 'books']

    def get_name(self, obj):
        return f"{obj.first_name} {obj.last_name}" #combines first_name and last_name into one field
    
    