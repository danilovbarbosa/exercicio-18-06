import pytest
from django.urls import reverse


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
    

def test_quando_acessar_update_entao_retonar_status_200(client):
    url = reverse("update")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_quando_acessar_update_entao_retonar_contudo_str_home(client):
    url = reverse("read")
    response = client.get(url)
    assert "Lista de pagamentos" in str(response.content)


