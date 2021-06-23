from django.test import TestCase

from financa.models import Pagamento
from financa.serializers import PagamentoSerializer


class TestPagamentoSerializer(TestCase):
    def setUp(self) -> None:
        super().setUp()

        self.atributos = {
            "id_pedido": 1,
            "id_vendedor": 1,
            "status_pedido": "FA",
            "valor_pedido": 1,
            "valor_delivery": 1,
        }

        self.serializer_data = {
            "id_pedido": 2,
            "id_vendedor": 2,
            "status_pedido": "RE",
            "valor_pedido": 2,
            "valor_delivery": 2,
        }

        self.objeto = Pagamento.objects.create(**self.atributos)
        self.objeto_serializer = PagamentoSerializer(instance=self.objeto)

    def test_contains_expected_fields(self):
        data = self.objeto_serializer.data

        self.assertEqual(
            set(data.keys()),
            set(
                [
                    "id",
                    "id_pedido",
                    "id_vendedor",
                    "status_pedido",
                    "valor_pedido",
                    "valor_delivery",
                ]
            ),
        )
