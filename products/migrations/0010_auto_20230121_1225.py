# Generated by Django 3.2 on 2023-01-21 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20230104_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='live',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]