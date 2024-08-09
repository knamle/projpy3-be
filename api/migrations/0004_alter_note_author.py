# Generated by Django 5.0.7 on 2024-08-05 10:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='api.user'),
        ),
    ]
