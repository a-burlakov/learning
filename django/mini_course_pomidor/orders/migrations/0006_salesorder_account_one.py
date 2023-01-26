# Generated by Django 4.1.5 on 2023-01-26 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_producttype'),
        ('orders', '0005_salesorder_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorder',
            name='account_one',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='products.product'),
        ),
    ]
