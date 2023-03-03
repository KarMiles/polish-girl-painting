# Generated by Django 3.2 on 2023-03-03 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_checkoutsettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutsettings',
            name='delivery_min_charge',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='checkoutsettings',
            name='free_delivery_threshold',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='checkoutsettings',
            name='standard_delivery_percentage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
