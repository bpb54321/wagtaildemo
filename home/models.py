from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.models import Image, AbstractImage, AbstractRendition


class CustomImage(AbstractImage):
    # Add any extra fields to image here

    caption = models.CharField(max_length=255, blank=True)

    admin_form_fields = Image.admin_form_fields + (
        # Then add the field names here to make them appear in the form:
        'caption',
    )


class CustomRendition(AbstractRendition):
    image = models.ForeignKey(
        CustomImage, on_delete=models.CASCADE, related_name='renditions'
    )

    class Meta:
        unique_together = (
            ('image', 'filter_spec', 'focal_point_key'),
        )


class CarouselItemBlock(blocks.StructBlock):
    heading = blocks.CharBlock()
    text = blocks.RichTextBlock()
    button_text = blocks.CharBlock()
    button_link = blocks.URLBlock()
    background_image = ImageChooserBlock()

    class Meta:
        template = 'blocks/carousel_item_block.html'


class HomePage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('carousel_items', blocks.ListBlock(CarouselItemBlock(),
            template='blocks/carousel_items.html')),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
