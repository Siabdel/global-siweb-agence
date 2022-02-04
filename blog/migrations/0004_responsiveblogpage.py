# Generated by Django 3.1.10 on 2021-09-13 09:11

from django.db import migrations, models
import django.db.models.deletion
import streamfieldblocks.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('blog', '0003_blogpagegalleryimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResponsiveBlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('main_content', wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('responsive_image', streamfieldblocks.models.ResponsiveImageBlock()), ('card', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(requierd=False)), ('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.TextBlock()), ('page_link', wagtail.core.blocks.PageChooserBlock())]))], blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]