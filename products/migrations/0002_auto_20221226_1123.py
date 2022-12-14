# Generated by Django 3.2 on 2022-12-26 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='priority',
            field=models.CharField(blank=True, choices=[('1 - Top', 'Top'), ('2 - High', 'High'), ('3 - Normal', 'Normal'), ('4 - Low', 'Low'), ('5 - Lowest', 'Lowest')], default='3 - Normal', max_length=10, null=True),
        ),
    ]
