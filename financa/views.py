from django.shortcuts import render


def create(request):
    context = {
        "title_page": "Criar pagamento",
    }
    return render(request, "", context=context)


def read(request):
    context = {
        "title_page": "Criar pagamento",
    }
    return render(request, "", context=context)


def update(request):
    context = {
        "title_page": "Atualizar pagamento",
    }
    return render(request, "", context=context)


def delete(request):
    context = {}
    return render(request, "", context=context)
