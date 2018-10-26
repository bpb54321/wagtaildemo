from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock


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
        ('carousel_items', blocks.ListBlock(
                CarouselItemBlock(),
                template='blocks/carousel_items.html',
            )
        ),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
