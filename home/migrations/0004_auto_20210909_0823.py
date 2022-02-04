# Generated by Django 3.1.10 on 2021-09-09 08:23

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='body',
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_body',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
    ]