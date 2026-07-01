from django.db import models
from books.models import Book
from members.models import Member

# Create your models here.

class BorrowRecord(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book= models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.member} borrowed {self.book.title}"