from django.test import TestCase
from app.app.cal import add


class CalTests(TestCase):

    def test_add_numbers(self):
        """Test that tow numbers are added together"""
        self.assertEqual(add(3, 8), 11)
