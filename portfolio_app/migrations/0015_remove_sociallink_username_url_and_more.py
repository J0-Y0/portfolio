# Generated by Django 5.1.1 on 2024-11-15 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0014_rename_social_logo_sociallink_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sociallink',
            name='username_url',
        ),
        migrations.AddField(
            model_name='sociallink',
            name='your_address',
            field=models.CharField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
