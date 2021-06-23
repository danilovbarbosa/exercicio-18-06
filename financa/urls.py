from django.urls import path, include

from rest_framework import routers

from financa import views

router = routers.DefaultRouter()
router.register(r"pagamentos", views.PagamentoViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("create/", views.create, name="create"),
    path("read/", views.read, name="read"),
    path("update/<int:id>", views.update, name="update"),
    path("delete/<int:id>", views.delete, name="delete"),
]
