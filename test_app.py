# test_app.py
import unittest
from app import suma, resta

class TestApp(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(3, 5), 8)

    def test_resta(self):
        self.assertEqual(resta(10, 5), 5)

if __name__ == '__main__':
    unittest.main()
