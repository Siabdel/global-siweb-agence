# Generated by Django 3.1.10 on 2021-09-09 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210909_0823'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
