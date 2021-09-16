import unittest

from simple_script import hello


class TestSimpleThings(unittest.TestCase):

	def test_hello_returns_42(self):
		value = hello()
		self.assertEqual(value, 42)