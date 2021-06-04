from exercisefunctions import anagram
import pytest

def test_checkanagram_true():
    a = "Blueband"
    b = "Bandblue"
    result = anagram.checkanagram(a,b)
    assert result == True

def test_checkanagram_false():
    a = "Blueband"
    b = "Greenband"
    result = anagram.checkanagram(a,b)
    assert result == False
