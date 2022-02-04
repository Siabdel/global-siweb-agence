from django.db import models
from wagtail.images.blocks import  ImageChooserBlock
from wagtail.core import blocks
# Create your models here.

class ResponsiveImageBlock(ImageChooserBlock):
    class Meta:
        icon = 'image'
        template = "streamfieldblocks/responsive_image_block.html"


class CardBlock(blocks.StructBlock):
    image = ImageChooserBlock(requierd=False)
    title = blocks.CharBlock() 
    body = blocks.TextBlock() 
    #page_link = blocks.PageChooserBlock() 
    
    class Meta:
        icon = 'image'
        template = "streamfieldblocks/card_block.html"    