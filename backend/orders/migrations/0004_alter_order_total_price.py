# Generated by Django 5.1.7 on 2025-05-14 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.PositiveBigIntegerField(blank=True, default=0, null=True),
        ),
    ]
