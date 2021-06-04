# Writing a function that brings back count of all alphabets of a given word
import collections as col


def alphabetcounter_dict(word):
    wordcount = {}
    for alphabet in word:
        if alphabet in wordcount:
            wordcount[alphabet] += 1
        else:
            wordcount[alphabet] = 1
    return wordcount


def alphabetcounter_collections(word):
    wordcount = col.Counter(word)
    return wordcount
