import pytest
from django.urls import reverse

from financa.models import Pagamento
from financa.forms import PagamentoForm


@pytest.fixture
def obj_pagamento():
    pagamento = Pagamento.objects.create(
        id_pedido=1,
        id_vendedor=1,
        status_pedido="FA",
        valor_pedido=1,
        valor_delivery=1,
    )
    return pagamento


@pytest.mark.django_db
def test_quando_acessar_create_entao_retonar_status_200(client):
    url = reverse("create")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_quando_acessar_create_entao_retonar_contudo_str_home(client):
    url = reverse("create")
    response = client.get(url)
    assert "Criar pagamento" in str(response.content)


@pytest.mark.django_db
def test_quando_acessar_read_entao_retonar_status_200(client):
    url = reverse("read")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_quando_acessar_read_entao_retonar_contudo_str_home(client):
    url = reverse("read")
    response = client.get(url)
    assert "Lista de pagamentos" in str(response.content)


@pytest.mark.django_db
def test_valid_form(obj_pagamento):
    data = {
        "id_pedido": obj_pagamento.id_pedido,
        "id_vendedor": obj_pagamento.id_vendedor,
        "status_pedido": obj_pagamento.status_pedido,
        "valor_pedido": obj_pagamento.valor_pedido,
        "valor_delivery": obj_pagamento.valor_delivery,
    }

    form = PagamentoForm(data=data)

    assert form.is_valid() == True
