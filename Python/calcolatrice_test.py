import unittest
from calcolatrice import somma


class TestCalcolatrice(unittest.TestCase):
    def test_somma(self):
        self.assertEqual(somma(4, 2), 7)

if __name__ == '__main__':
    unittest.main()