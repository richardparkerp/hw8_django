# Generated by Django 5.0.2 on 2024-02-26 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='street',
            name='number',
            field=models.IntegerField(default=1),
        ),
    ]
