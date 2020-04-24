import unittest
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.App()

    def test_hello(self):
        self.assertEqual(self.app.hello_string, 'Hello World')

