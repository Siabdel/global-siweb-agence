# Generated by Django 3.1.10 on 2021-09-10 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpage',
            old_name='date',
            new_name='created',
        ),
    ]