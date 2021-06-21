from django.test import TestCase
import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_quando_acessar_home_entao_retonar_status_200(client):
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_quando_acessar_home_entao_retonar_contudo_str_home(client):
    url = reverse("home")
    response = client.get(url)
    assert "Home" in str(response.content)


class TestPageHome(TestCase):
    def test_quando_acessar_url_home_entao_retonar_template_home(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "base.html")
        self.assertContains(response, "Home")
