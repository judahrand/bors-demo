from unittest import TestCase

from src import main

class TestMain(TestCase):
    def test_bifurateCrab(self):
        self.assertTrue(main.bifurcateCrab())

    def test_drive(self):
        self.assertTrue(main.drive())

    def test_onland(self):
        self.assertTrue(main.onland())
