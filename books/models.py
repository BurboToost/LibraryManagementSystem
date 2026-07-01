from django.db import models
from authors.models import Author
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pub_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[('Available', 'Available'), ('Borrowed', 'Borrowed')],
        default='Available'
    )

    def __str__(self):
        return self.title   