from django.shortcuts import render

from authors.models import Author
from books.models import Book
from borrowing.models import BorrowRecord
from members.models import Member


def home(request):
    books_total = Book.objects.count()
    available_books = Book.objects.filter(status='Available').count()
    borrowed_books = Book.objects.filter(status='Borrowed').count()

    context = {
        'authors_total': Author.objects.count(),
        'books_total': books_total,
        'available_books': available_books,
        'borrowed_books': borrowed_books,
        'members_total': Member.objects.count(),
        'borrow_records_total': BorrowRecord.objects.count(),
    }
    return render(request, 'home.html', context)