# Generated by Django 4.0.1 on 2022-01-30 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_note',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]