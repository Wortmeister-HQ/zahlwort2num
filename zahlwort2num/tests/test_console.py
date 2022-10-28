from _ctypes import ArgumentError

from unittest import TestCase
from zahlwort2num.command_line import main


class TestConsole(TestCase):
    def test_basic(self):
        self.assertRaises(ArgumentError, main)
