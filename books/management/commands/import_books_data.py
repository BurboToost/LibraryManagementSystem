import json
from datetime import date
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from authors.models import Author
from books.models import Book


class Command(BaseCommand):
    help = "Import authors and books from books_data.json into the database."

    def handle(self, *args, **options):
        data_path = Path(settings.BASE_DIR) / "books_data.json"

        if not data_path.exists():
            raise CommandError(f"Data file not found: {data_path}")

        with data_path.open("r", encoding="utf-8-sig") as data_file:
            records = json.load(data_file)

        imported_authors = 0
        imported_books = 0

        for record in records:
            author_name = record["author_name"].strip()
            biography = record.get("author_biography", "").strip()
            title = record["title"].strip()
            publication_date = date.fromisoformat(record["publication_date"])
            status = record.get("status", "Available")

            author, author_created = Author.objects.update_or_create(
                name=author_name,
                defaults={"biography": biography},
            )
            if author_created:
                imported_authors += 1

            _, book_created = Book.objects.update_or_create(
                title=title,
                author=author,
                defaults={
                    "pub_date": publication_date,
                    "status": status,
                },
            )
            if book_created:
                imported_books += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Imported {imported_authors} authors and {imported_books} books from books_data.json."
            )
        )