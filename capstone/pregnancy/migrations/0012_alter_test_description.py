# Generated by Django 4.2.7 on 2023-12-26 03:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pregnancy", "0011_rename_week_test_trimester_remove_test_done_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="test",
            name="description",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]