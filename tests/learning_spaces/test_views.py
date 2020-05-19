import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_reservation_list_view():
    instance1 = test_helpers.create_learning_spaces_reservation()
    instance2 = test_helpers.create_learning_spaces_reservation()
    client = Client()
    url = reverse("learning_spaces_reservation_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_reservation_create_view():
    client = Client()
    url = reverse("learning_spaces_reservation_create")
    data = {
        "end_time": datetime.now(),
        "start_time": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_reservation_detail_view():
    client = Client()
    instance = test_helpers.create_learning_spaces_reservation()
    url = reverse("learning_spaces_reservation_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_reservation_update_view():
    client = Client()
    instance = test_helpers.create_learning_spaces_reservation()
    url = reverse("learning_spaces_reservation_update", args=[instance.pk, ])
    data = {
        "end_time": datetime.now(),
        "start_time": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_room_list_view():
    instance1 = test_helpers.create_learning_spaces_room()
    instance2 = test_helpers.create_learning_spaces_room()
    client = Client()
    url = reverse("learning_spaces_room_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_room_create_view():
    client = Client()
    url = reverse("learning_spaces_room_create")
    data = {
        "description": "text",
        "location": "text",
        "size": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_room_detail_view():
    client = Client()
    instance = test_helpers.create_learning_spaces_room()
    url = reverse("learning_spaces_room_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_room_update_view():
    client = Client()
    instance = test_helpers.create_learning_spaces_room()
    url = reverse("learning_spaces_room_update", args=[instance.pk, ])
    data = {
        "description": "text",
        "location": "text",
        "size": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302
