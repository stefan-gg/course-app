# Generated by Django 4.1.8 on 2023-04-22 01:07

import courses.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("short_description", models.CharField(max_length=256)),
                ("description", models.CharField(max_length=1024)),
                ("price", models.FloatField()),
                (
                    "course_image",
                    models.ImageField(
                        max_length=256,
                        upload_to=courses.models.upload_image_to,
                        verbose_name="Course headline image",
                    ),
                ),
                (
                    "author_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
