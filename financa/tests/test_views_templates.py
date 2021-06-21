from django.test import TestCase
from django.urls import reverse

from financa.models import Pagamento

class TestPageHome(TestCase):
    def setUp(self) -> None:
        super().setUp()
        Pagamento.objects.create(
            id_pedido = 1,
            id_vendedor = 1,
            status_pedido = 'FA',
            valor_pedido = 1,
            valor_delivery = 1,
        )
    
    def test_quando_acessar_url_create_entao_retonar_template_financa_form(
        self,
    ):
        url = reverse("create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "financa_form.html")

    def test_quando_acessar_url_read_entao_retonar_template_financa_list(self):
        url = reverse("read")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "financa_list.html")

# TODO: Finalizar.
    # def test_quando_acessar_url_update_entao_retonar_template_financa_form(
    #     self,
    # ):
    #     pagamento = Pagamento.objects.get(id_pedido="1")

    #     url = reverse("update", kwargs={'pk': pagamento.id})
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, "financa_form.html")

    # def test_quando_acessar_url_delete_entao_retonar_template_financa_list(
    #     self,
    # ):
    #     # url = reverse("delete", kwargs={'pk': self.pagamento.id})
    #     url = '/delete/'
    #     pagamento = Pagamento.objects.get(id_pedido="1")

    #     response = self.client.get(url, {'id': pagamento.id})
    #     self.assertRedirects(
    #         response, reverse("read"), status_code=200, target_status_code=200
    #     )
