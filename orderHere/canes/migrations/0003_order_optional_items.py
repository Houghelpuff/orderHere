# Generated by Django 3.0.6 on 2020-05-28 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canes', '0002_order_drink'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='optional_items',
            field=models.ManyToManyField(related_name='_order_optional_items_+', to='canes.Order'),
        ),
    ]
