# Generated by Django 4.0.6 on 2022-07-18 10:28

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='author',
            managers=[
                ('top_author_managers', django.db.models.manager.Manager()),
            ],
        ),
    ]
