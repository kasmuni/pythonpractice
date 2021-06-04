from exercisefunctions import alphabetcounter
import pytest

#Setting up the word and expected result for further tests
@pytest.fixture()
def setup():
    word = "supercalifragilisticexpialidocious"
    expectedresult = {'a': 3, 'c': 3, 'd': 1, 'e': 2, 'f': 1, 'g': 1, 'i': 7,
                      'l': 3, 'o': 2, 'p': 2, 'r': 2, 's': 3,
                      't': 1, 'u': 2, 'x': 1}

    return word, expectedresult

# Test function for counting through dictionary
def test_alphabetcounter_dict(setup):
    word = setup[0]
    expectedresult = setup[1]
    result = alphabetcounter.alphabetcounter_dict(word)
    assert result == expectedresult

# Test function for counting through collections counter
def test_alphabetcounter_collections(setup):
    word = setup[0]
    expectedresult = setup[1]
    result = alphabetcounter.alphabetcounter_collections(word)
    assert result == expectedresult