# Generated by Django 3.0.3 on 2020-04-13 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_auto_20200413_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='CatParent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Category'),
        ),
    ]
