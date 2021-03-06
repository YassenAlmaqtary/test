# Generated by Django 3.0.3 on 2020-04-16 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BRDName', models.CharField(max_length=40)),
                ('BRDDesc', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VarName', models.CharField(max_length=40)),
                ('VarDesc', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Variant',
                'verbose_name_plural': 'Variants',
            },
        ),
    ]
