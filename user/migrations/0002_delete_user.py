# Generated by Django 4.0.3 on 2022-09-08 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_alter_document_author'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
