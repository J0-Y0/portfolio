# Generated by Django 5.1.5 on 2025-05-04 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0035_alter_project_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='projects', to='portfolio_app.tag'),
        ),
    ]
