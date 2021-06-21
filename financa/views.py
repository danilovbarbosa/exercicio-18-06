from django.shortcuts import render, redirect
from financa.forms import PagamentoForm
from financa.models import Pagamento


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
        "title_page": "Criar pagamento",
        "list_objetos": list_objetos,
    }
    return render(request, "financa_list.html", context=context)


def update(request, post_id):
    post_object = Pagamento.objects.get(id=post_id)
    formulario = PagamentoForm(request.POST or None, instance=post_object)

    if formulario.is_valid():
        formulario.save()

        return redirect("read")
    context = {
        "title_page": "Atualizar pagamento",
        "post": formulario,
    }
    return render(request, "financa_list.html", context=context)


def delete(request, post_id):
    Pagamento.objects.get(id=post_id).delete()
    return redirect("read")
