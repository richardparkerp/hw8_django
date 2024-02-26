# Generated by Django 5.0.2 on 2024-02-26 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('secapp', '0001_initial'), ('secapp', '0002_street_number')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.IntegerField(default=1)),
            ],
        ),
    ]
