# Generated by Django 3.2.4 on 2021-06-21 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pedido', models.IntegerField()),
                ('id_vendedor', models.IntegerField()),
                ('status_pedido', models.CharField(choices=[('FA', 'Faturado'), ('RE', 'Recebido Olist'), ('PS', 'Pago ao Seller'), ('CA', 'Cancelado')], default='FA', max_length=2)),
                ('valor_pedido', models.DecimalField(decimal_places=10, max_digits=19)),
                ('valor_delivery', models.DecimalField(decimal_places=10, max_digits=19)),
            ],
        ),
    ]