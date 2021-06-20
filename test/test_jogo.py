from typing import List
from unittest import TestCase
from ap_qt import J3A7P6

class jogo(TestCase):

    def setUp(self):
        self.app = J3A7P6()

    def test_verifi_palavra(self):
        self.assertTrue(self.app.palavras)
        print(self.app.palavras)