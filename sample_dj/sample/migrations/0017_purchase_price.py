# Generated by Django 4.1.5 on 2023-02-09 14:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sample", "0016_purchase"),
    ]

    operations = [
        migrations.AddField(
            model_name="purchase",
            name="price",
            field=models.IntegerField(default=0),
        ),
    ]
