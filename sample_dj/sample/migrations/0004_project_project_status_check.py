# Generated by Django 4.1.5 on 2023-02-01 04:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sample", "0003_project_project_lesson_unique"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="project",
            constraint=models.CheckConstraint(
                check=models.Q(("status__in", ["finished", "waiting"])),
                name="project_status_check",
            ),
        ),
    ]