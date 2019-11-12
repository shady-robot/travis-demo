from django.test import TestCase


class FailTests(TestCase):
    def test_mean_to_fail(self):
        self.assertEqual(1, 3)
