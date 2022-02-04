from streamfieldblocks.models import ResponsiveImageBlock, CardBlock
from django.db import models

# Create your models here.
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from django.db import models
from wagtail.search import index
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey
from wagtail.core  import blocks
from wagtail.images.blocks import ImageChooserBlock, ImageChooserBlockComparison
from wagtail.core.fields import RichTextField, StreamField

# Keep the definition of BlogIndexPage, and add:


class BlogPage(Page):
    created = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('created'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Gallery images"),
    ]
    
## class gallery image    
class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
## page list des articles
class BlogIndexPage(Page):
    
    def get_context(self, request):
          # Update context to include only published posts, ordered by reverse-chron
      context = super().get_context(request)
      articles = self.get_children().live().order_by('-first_published_at')
      context['articles'] = articles
      return context
  
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]



#--  blog : structBlocks
class  ResponsiveBlogPage(Page):
    created = models.DateField("Date Article")
    intro = models.TextField("Introduction")
    main_content = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('responsive_image', ResponsiveImageBlock()),
        ('card', CardBlock()),
    ], blank=True)
    featured = models.BooleanField(default=False)

    content_panels = Page.content_panels + [
        FieldPanel('created'),
        FieldPanel('featured'),
        FieldPanel('intro'),
        StreamFieldPanel('main_content'),
    ]


#--------------------------------
#---- Blog
#--------------------------------

class StreamBlogPage(Page):
    author = models.CharField(max_length=255)
    date = models.DateField("Post date")
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('card', CardBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        StreamFieldPanel('body'),
    ]