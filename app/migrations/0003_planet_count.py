# Generated by Django 5.0.2 on 2024-02-26 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_planet_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
