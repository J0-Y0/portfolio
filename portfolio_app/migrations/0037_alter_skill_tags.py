# Generated by Django 5.1.5 on 2025-05-04 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0036_alter_project_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='skills', to='portfolio_app.tag'),
        ),
    ]
