from django.db import models


class Category(models.Model):
    title = models.CharField(
        max_length=50, help_text='Limited to 50 characters.')
    slug = models.SlugField(
        help_text='Suggested value automatically generated from title.')
    description = models.TextField(
        help_text='A brief description of the content being categorized. '
                  'No HTML is allowed.', blank=True)
    lead_image = models.ImageField(
        upload_to='images/lead_images',
        help_text='Upload an image to display as the lead image on the '
                  'template. Image must be cropped for display at 1170px wide,'
                  ' 400px tall. Please use JPG or PNG formats. Will populate '
                  'the width and height fields on save.',
        width_field='lead_image_width',
        height_field='lead_image_height',
        blank=True
    )
    lead_image_width = models.PositiveIntegerField(blank=True, null=True)
    lead_image_height = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.title
