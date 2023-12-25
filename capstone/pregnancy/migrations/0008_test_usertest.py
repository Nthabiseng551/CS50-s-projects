# Generated by Django 4.2.7 on 2023-12-25 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("pregnancy", "0007_alter_userprofile_week_update_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="Test",
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
                ("test_name", models.CharField(max_length=100)),
                ("week", models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserTest",
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
                ("done", models.BooleanField(default=False)),
                (
                    "test",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="usertests",
                        to="pregnancy.test",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tests",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]