# Generated by Django 4.0.1 on 2022-01-31 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_order_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='color',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='size',
        ),
    ]