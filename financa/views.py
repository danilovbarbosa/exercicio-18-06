from django.shortcuts import render
from financa.models import Pagamento

def create(request):

    context = {
        "title_page": "Criar pagamento",
    }
    return render(request, "", context=context)


def read(request):
    list_objetos = Pagamento.objects.all()

    context = {
        "title_page": "Criar pagamento",
        "list_objetos" : list_objetos,
    }
    return render(request, "financa_list.html", context=context)


def update(request):
    context = {
        "title_page": "Atualizar pagamento",
    }
    return render(request, "", context=context)


def delete(request):
    context = {}
    return render(request, "", context=context)
