# Generated by Django 5.0.3 on 2024-03-12 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passwordmanager', '0005_alter_passwordsmanagermodel_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordsmanagermodel',
            name='username',
            field=models.TextField(),
        ),
    ]
