# Generated by Django 5.0.4 on 2024-04-26 09:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_comment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="comment_text",
            new_name="text",
        ),
    ]
