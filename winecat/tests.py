from django.test import TestCase

# Create your tests here.

import datetime

from django.utils import timezone

from .models import Wine


class WineModelTests(TestCase):
    def test_wine_age(self):
        """
        the appellation view should show the correct wines
        """
        wine = Wine(year='2017')
        self.assertIs(wine.how_old_is_it(), 5)
