from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE) #one-to-many relationship

    def clean(self):
        # Customising validation to make sure publication year is not in the future.
        if self.publication_year > date.today().year:
            raise ValidationError("Publication year should be in the past and not future")
        
    def __str__(self):
        return f"{self.title} ({self.publication_year})"
  