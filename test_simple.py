import unittest

from simple_script import hello, greetings


class TestSimpleThings(unittest.TestCase):

	def test_hello_returns_42(self):
		value = hello()
		self.assertEqual(value, 42)

	def test_greetings_returns_43(self):
		value = greetings()
		self.assertEqual(value, 43)