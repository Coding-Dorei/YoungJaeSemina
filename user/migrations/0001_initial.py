# Generated by Django 4.0.3 on 2022-09-06 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=20)),
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
