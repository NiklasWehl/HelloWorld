import unittest

# Funktion, die getestet werden soll
def add(a, b):
    return a + b

# Testklasse, die von unittest.TestCase erbt
class TestAddFunction(unittest.TestCase):

    # Testmethoden beginnen mit "test_"
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-1, 1), 0)

# Dies führt den Test aus, wenn das Skript direkt ausgeführt wird
if __name__ == '__main__':
    unittest.main()