# Generated by Django 3.1.1 on 2020-09-22 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200922_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='last_modified',
        ),
    ]
