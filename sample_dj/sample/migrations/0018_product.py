# Generated by Django 4.1.5 on 2023-02-11 15:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sample", "0017_purchase_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=100)),
                ("price", models.IntegerField()),
            ],
        ),
    ]
