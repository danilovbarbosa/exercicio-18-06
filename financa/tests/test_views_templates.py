from django.test import TestCase
from django.urls import reverse


class TestPageHome(TestCase):
    def test_quando_acessar_url_create_entao_retonar_template_financa_form(self):
        url = reverse("create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "financa_form.html")

    def test_quando_acessar_url_read_entao_retonar_template_financa_list(self):
        url = reverse("read")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "financa_list.html")

    def test_quando_acessar_url_update_entao_retonar_template_financa_form(self):
        url = reverse("update")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "financa_form.html")

    def test_quando_acessar_url_delete_entao_retonar_template_financa_list(self):
        url = reverse("delete")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "financa_list.html")
