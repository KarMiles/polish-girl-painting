# Generated by Django 3.2 on 2023-02-14 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='priority',
            field=models.CharField(blank=True, choices=[('1 - Top', 'Top'), ('2 - High', 'High'), ('3 - Normal', 'Normal'), ('4 - Low', 'Low'), ('5 - Lowest', 'Lowest')], default='3 - Normal', max_length=10, null=True),
        ),
    ]
