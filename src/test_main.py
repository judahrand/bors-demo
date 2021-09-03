from unittest import TestCase

from src import main

class TestMain(TestCase):
    def test_bifurate(self):
        self.assertTrue(main.bifurcate())

    def test_drive(self):
        self.assertTrue(main.drive())

    def test_onland(self):
        self.assertTrue(main.onland())

    def test_park(self):
        self.assertTrue(main.park())
