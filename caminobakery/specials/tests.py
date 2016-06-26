from test_plus import TestCase
import factory
from freezegun import freeze_time

from .models import Special


class SpecialFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'specials.Special'


class SpecialModelTests(TestCase):

    def setUp(self):
        self.special_monday = SpecialFactory.create(
            description='free beer',
            day_offered=Special.MONDAY_SPECIAL
        )
        self.special_tuesday = SpecialFactory.create(
            description='free hair',
            day_offered=Special.TUESDAY_SPECIAL
        )
        self.special_saturday = SpecialFactory.create(
            description='free cats',
            day_offered=Special.SATURDAY_SPECIAL
        )

    def tearDown(self):
        [s.delete() for s in Special.objects.all()]

    @freeze_time("2016-06-25")
    def test_special_today_manager(self):
        "Should return specials for a Saturday."
        self.assertEqual(Special.today.count(), 1)
