# Generated by Django 5.0.6 on 2024-11-06 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio_app", "0002_tag_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="slug",
            field=models.SlugField(default="hrllo-h-e", unique=True),
            preserve_default=False,
        ),
    ]
