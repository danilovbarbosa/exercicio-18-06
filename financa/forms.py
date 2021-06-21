from django.forms import ModelForm
from financa.models import Pagamento


class PagamentoForm(ModelForm):
    class Meta:
        model = Pagamento
        fields = "__all__"