import unittest
class TestSamples(unittest.TestCase):
    
    def test_check_boolean(self):
        self.assertTrue(1==2)

    def test_compare_numbers(self):
        self.assertEqual(2,2)

    def test_compare_strings(self):
        self.assertEqual("abc", "abc")

    def test_compare_arrays(self):
        self.assertEqual([1,2,3],[1,2,3])
