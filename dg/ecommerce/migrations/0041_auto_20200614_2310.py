# Generated by Django 3.0.6 on 2020-06-14 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0040_auto_20200614_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='C_order_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
