from django.shortcuts import render


def create(request):
    context = {}
    return render(request, "", context=context)


def read(request):
    context = {}
    return render(request, "", context=context)


def update(request):
    context = {}
    return render(request, "", context=context)


def delete(request):
    context = {}
    return render(request, "", context=context)
