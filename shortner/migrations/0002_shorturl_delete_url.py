# Generated by Django 4.2.2 on 2023-09-03 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shortner", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ShortUrl",
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
                ("original_url", models.URLField(max_length=7000)),
                ("short_url", models.CharField(max_length=100)),
                ("time_date_created", models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(name="Url",),
    ]
