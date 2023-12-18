
# TDD - фреймворк (не менее 3 тестов).

import unittest
from main import LevenshteinDistance

class TestLevenshteinDistance(unittest.TestCase):
    def test_distance_equal_strings(self):
        levenshtein = LevenshteinDistance()
        self.assertEqual(levenshtein.dist("kitten", "kitten"), 0)

    def test_distance_different_strings(self):
        levenshtein = LevenshteinDistance()
        self.assertEqual(levenshtein.dist("kitten", "sitting"), 3)

    def test_distance_empty_string(self):
        levenshtein = LevenshteinDistance()
        self.assertEqual(levenshtein.dist("", "abc"), 3)

if __name__ == '__main__':
    unittest.main()



