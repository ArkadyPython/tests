from ya_disc import *
from unittest import TestCase
class TestYandex(TestCase):
    def test_get_upload(self):
        self.assertEqual(ex.get_upload('can'), 201, "folder created")


