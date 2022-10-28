from unittest import TestCase

from zahlwort2num.command_line import *

class TestConsole(TestCase):
    def test_basic(self):
        self.assertRaises(ArgumentError, main)