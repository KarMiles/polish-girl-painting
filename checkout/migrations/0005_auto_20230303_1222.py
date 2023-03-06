# Generated by Django 3.2 on 2023-03-03 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20230303_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutsettings',
            name='delivery_min_charge',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='checkoutsettings',
            name='free_delivery_threshold',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='checkoutsettings',
            name='standard_delivery_percentage',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]