# Generated by Django 4.1.5 on 2023-02-03 08:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sample", "0010_item_shop"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
