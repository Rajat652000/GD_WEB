# Generated by Django 5.1.5 on 2025-03-14 14:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="machines",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AddField(
            model_name="machines",
            name="uploaded_at",
            field=models.DateTimeField(
                default=datetime.datetime(2025, 3, 14, 20, 4, 53, 307520)
            ),
        ),
    ]
