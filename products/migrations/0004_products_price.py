# Generated by Django 4.2.6 on 2024-02-20 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_products_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='Цена'),
        ),
    ]
