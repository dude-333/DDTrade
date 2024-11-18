# Generated by Django 5.1.3 on 2024-11-18 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_stock_name_alter_stock_yfinance_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockdetails',
            name='yfinance_name',
        ),
        migrations.AlterField(
            model_name='stockdetails',
            name='closing_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]