import factory
from factory.django import DjangoModelFactory
from main.models import Book


class BookFactory(DjangoModelFactory):
    class Meta:
        model = Book

    name = factory.Faker("text", max_nb_chars=20)
    author = factory.Faker("name")
    year_published = factory.Faker("pyint", min_value=0, max_value=2023)
    isbn = factory.Faker("isbn13")
