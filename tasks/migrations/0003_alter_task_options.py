# Generated by Django 5.0.2 on 2024-02-19 17:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0002_alter_tag_options_alter_task_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={
                "ordering": ("is_done", "created_at"),
                "verbose_name": "task",
                "verbose_name_plural": "tasks",
            },
        ),
    ]
