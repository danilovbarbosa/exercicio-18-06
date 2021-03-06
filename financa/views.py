from django.shortcuts import get_object_or_404, render, redirect

from rest_framework import viewsets

from financa.forms import PagamentoForm
from financa.models import Pagamento
from financa.serializers import PagamentoSerializer


# Views DRF
class PagamentoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Pagamento.objects.all().order_by("-id_pedido")
    serializer_class = PagamentoSerializer


# Views Django
def create(request):
    formulario = PagamentoForm(request.POST or None)

    if formulario.is_valid():
        formulario.save()

        return redirect("read")

    context = {
        "title_page": "Criar pagamento",
        "post": formulario,
    }
    return render(request, "financa_form.html", context=context)


def read(request):
    list_objetos = Pagamento.objects.all()

    context = {
        "title_page": "Lista de pagamentos",
        "list_objetos": list_objetos,
    }
    return render(request, "financa_list.html", context=context)


def update(request, id):
    post_object = Pagamento.objects.get(id=id)
    formulario = PagamentoForm(request.POST or None, instance=post_object)

    if formulario.is_valid():
        formulario.save()

        return redirect("read")
    context = {
        "title_page": "Atualizar pagamento",
        "post": formulario,
    }
    return render(request, "financa_form.html", context=context)


def delete(request, id):
    objeto = get_object_or_404(Pagamento, id=id)
    objeto.delete()
    return redirect("read")
