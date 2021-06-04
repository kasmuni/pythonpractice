# Creating anagram function that checks if two strings have same characters in them

import collections as col

def checkanagram(a,b):
    # Using list comprehension to make list of all characters in a and b strings
    charina = [x for x in a]
    charinb = [y for y in b]

    # Using the collection module counter function to match unordered collection
    if col.Counter(charina) == col.Counter(charinb):
        return True
    return False
