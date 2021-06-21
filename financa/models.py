from django.db import models


class Pagamento(models.Model):
    id_pedido = models.IntegerField()
    id_vendedor = models.IntegerField()

    FATURADO = "FA"
    RECEBIDO = "RE"
    PAGO_AO_SELLER = "PS"
    CANCELADO = "CA"

    STATUS_PAGAMENTO_CHOICES = [
        (FATURADO, "Faturado"),
        (RECEBIDO, "Recebido Olist"),
        (PAGO_AO_SELLER, "Pago ao Seller"),
        (CANCELADO, "Cancelado"),
    ]
    status_pedido = models.CharField(
        max_length=2,
        choices=STATUS_PAGAMENTO_CHOICES,
        default=FATURADO,
    )

    valor_pedido = models.DecimalField(max_digits=19, decimal_places=10)
    valor_delivery = models.DecimalField(max_digits=19, decimal_places=10)
