from main import LevenshteinDistance
# Тесты с использованием pytest (BDD)

import pytest

@pytest.fixture
def levenshtein_distance():
    return LevenshteinDistance()

def test_distance_equal_strings(levenshtein_distance):
    assert levenshtein_distance.dist("kitten", "kitten") == 0

def test_distance_different_strings(levenshtein_distance):
    assert levenshtein_distance.dist("kitten", "sitting") == 3

def test_distance_empty_string(levenshtein_distance):
    assert levenshtein_distance.dist("", "abc") == 3

if __name__ == '__main__':
    pytest.main()
