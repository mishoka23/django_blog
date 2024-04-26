# Generated by Django 5.0.4 on 2024-04-26 07:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="image_name",
        ),
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(null=True, upload_to="posts"),
        ),
    ]
