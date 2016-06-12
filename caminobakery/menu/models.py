from django.db import models

from categories.models import Category


class LiveItemManager(models.Manager):
    def get_query_set(self):
        return super(LiveItemManager, self).get_query_set().filter(
            status=self.model.LIVE_STATUS).filter(is_available=True)


class Item(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
    )
    name = models.CharField(
        max_length=250,
        help_text='Limited to 250 characters.'
    )
    slug = models.SlugField(
        unique=True,
        help_text='Suggested value automatically generated from name. '
                  'Must be unique.')
    description = models.TextField(
        help_text='A brief description of the item. No HTML is allowed.',
        blank=True)
    one_off_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="Use if item isn't available in different sizes. "
        "Amount cannot be larger than five digits. Don't use a dollar sign.",
        blank=True,
        null=True
    )
    status = models.IntegerField(
        choices=STATUS_CHOICES, default=DRAFT_STATUS)
    item_type = models.ForeignKey('ItemType')
    photo = models.ImageField(
        upload_to='images/menu/photos',
        width_field='width',
        height_field='height',
        help_text='Please use JPG or PNG formats. '
                  'Will populate the width and height fields on save.',
        blank=True
        )
    width = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    is_flourless = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    vegan_option_available = models.BooleanField(default=False)
    flourless_option_available = models.BooleanField(default=False)
    is_seasonal = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)

    objects = models.Manager()
    live = LiveItemManager()

    class Meta:
        verbose_name_plural = 'Items'
        ordering = ['name']

    def get_item_price(self):
        """
        Returns price for item.
        """
        return self.item_type.size.all()

    def __unicode__(self):
        return '%s' % self.name


class Size(models.Model):
    size = models.CharField(
        max_length=100,
        help_text='Limited to 100 characters. '
        'Use either numerical or text-based characters.'
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text='Amount cannot be larger than five digits. '
        'Don\'t use a dollar sign.'
    )
    description = models.TextField(
        help_text='A brief description of the size. No HTML is allowed.',
        blank=True
    )

    class Meta:
        verbose_name_plural = 'Sizes'
        ordering = ['price']

    def __unicode__(self):
        return '%s / $%s' % (self.size, self.price)


class ItemType(Category):
    size = models.ManyToManyField(Size, blank=True)

    class Meta:
        verbose_name_plural = 'Item types'

    def get_items_for_type(self):
        """
        Returns all live items for a given item type.
        """
        return Item.live.filter(item_type=self)

    def get_size_for_items(self):
        """
        Returns sizes (and prices) for items for item type.
        """
        return Size.objects.filter(itemtype=self)

    def __unicode__(self):
        return self.title


class ItemTypeGroup(Category):
    item_types = models.ManyToManyField(
        ItemType,
        help_text='Select the item types you want to group together.'
    )

    class Meta:
        verbose_name_plural = 'Item type groups'

    def get_itemtypes_for_itemtypegroup(self):
        """
        Returns itemtypes for an item type group.
        """
        return ItemType.objects.filter(itemtypegroup=self)

    def get_items_for_itemtypegroup(self):
        """
        Returns items for item type in an item type group.
        """
        return Item.live.filter(item_type__itemtypegroup=self)

    def get_size_for_items(self):
        """
        Returns sizes (and prices) for items for item type in an item type group.
        """
        return Size.objects.filter(itemtype__itemtypegroup=self)

    def __unicode__(self):
        return self.title


class BreadSchedule(models.Model):
    bread = models.ForeignKey(
        Item,
        limit_choices_to={'item_type__title': 'Bread'}
    )
    days_available = models.ManyToManyField('Day')

    class Meta:
        verbose_name_plural = 'Bread schedules'

    def __unicode__(self):
        return unicode(self.bread)

    def is_available_daily(self):
        "Returns whether a bread is available every day of the week."
        if self.days_available.count() == 7:
            return 'Baked fresh every day'


class Day(models.Model):
    day = models.CharField(
        max_length=50,
        help_text='Limited to 50 characters.'
    )

    def __unicode__(self):
        return unicode(self.day)
