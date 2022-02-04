from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import  FieldPanel


class HomePage(Page):
    
    banner_title = models.CharField(max_length=100, blank=True, null=True)
    banner_body = RichTextField(blank=True, null=True)
    content_panels = Page.content_panels + [ 
        FieldPanel('banner_title', classname="full"),
        FieldPanel('banner_body', classname="full") ] 