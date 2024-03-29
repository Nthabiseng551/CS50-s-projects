# Generated by Django 4.2.7 on 2023-11-29 11:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0002_listing"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="watchlist",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="userlist",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="listing",
            name="category",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name="listing",
            name="description",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="listing",
            name="image_url",
            field=models.URLField(blank=True, null=True),
        ),
    ]
