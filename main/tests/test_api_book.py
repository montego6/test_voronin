import pytest
from rest_framework import status
from rest_framework.test import APIClient
import factory
from main.models import Book
from main.serializers import BookSerializer
from factories import BookFactory
from django.urls import reverse


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def book():
    return BookFactory()


@pytest.mark.django_db
def test_create_book(client):
    data = factory.build(dict, FACTORY_CLASS=BookFactory)
    response = client.post(reverse('book-list'), data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Book.objects.last() is not None


@pytest.mark.django_db
def test_update_book(client, book):
    data = factory.build(dict, FACTORY_CLASS=BookFactory)
    response = client.put(reverse('book-detail', kwargs={'pk': book.id}), data)
   
    expected_data = {
        'id': book.id,
        'name': data['name'],
        'author': data['author'],
        'year_published': data['year_published'],
        'isbn': data['isbn'],
    }
    
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_data


@pytest.mark.django_db
def test_partial_update_book(client, book):
    data = factory.build(dict, FACTORY_CLASS=BookFactory)
    data.pop('year_published')
    data.pop('isbn')
    response = client.patch(reverse('book-detail', kwargs={'pk': book.id}), data)
   
    expected_data = {
        'id': book.id,
        'name': data['name'],
        'author': data['author'],
        'year_published': book.year_published,
        'isbn': book.isbn,
    }
    
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_data


@pytest.mark.django_db
def test_retrieve_book(client, book):
    response = client.get(reverse('book-detail', kwargs={'pk': book.id}))
   
    expected_data = {
        'id': book.id,
        'name': book.name,
        'author': book.author,
        'year_published': book.year_published,
        'isbn': book.isbn,
    }
    
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_data


@pytest.mark.django_db
def test_list_book(client):
    books = BookFactory.create_batch(9)
    
    response = client.get(reverse('book-list'))
   
    expected_data = BookSerializer(books, many=True).data
    
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_data


@pytest.mark.django_db
def test_delete_book(client, book):
    response = client.delete(reverse('book-detail', kwargs={'pk': book.id}))
   
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Book.objects.last() is None


@pytest.mark.django_db
def test_count_book(client):
     books = BookFactory.create_batch(9)
     response = client.get(reverse('book-count'))

     expected_data = {
         'count': 9
     }

     assert response.status_code == status.HTTP_200_OK
     assert response.data == expected_data