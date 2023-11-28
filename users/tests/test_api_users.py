from unittest.mock import patch
from django.urls import reverse
from django.contrib.auth import get_user_model
import pytest
import factory
from rest_framework import status
from rest_framework.test import APIClient
from users.tests.factories import UserFactory

User = get_user_model()


@pytest.fixture
def client():
    return APIClient()


@pytest.mark.django_db
def test_create_user(client):
    data = factory.build(dict, FACTORY_CLASS=UserFactory)

    with patch('users.serializers.send_welcome_letter.delay') as mock_task:
        response = client.post(reverse('user-create'), data)
        assert mock_task.called


    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.last() is not None