# Generated by Django 5.0.1 on 2024-12-18 00:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.company'),
        ),
    ]
