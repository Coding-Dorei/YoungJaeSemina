# Generated by Django 4.0.3 on 2022-09-08 11:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_alter_document_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
