# Generated by Django 5.0.3 on 2024-03-12 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passwordmanager', '0003_passwordsmanagermodel_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordsmanagermodel',
            name='url',
            field=models.URLField(),
        ),
    ]