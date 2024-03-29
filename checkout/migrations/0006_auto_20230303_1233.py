# Generated by Django 3.2 on 2023-03-03 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20230303_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutsettings',
            name='delivery_min_charge',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='checkoutsettings',
            name='free_delivery_threshold',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='checkoutsettings',
            name='standard_delivery_percentage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
