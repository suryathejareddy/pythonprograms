__author__ = 'Kalyan'

notes = '''
1. Read instructions for the function carefully and constraints carefully.
2. Try to generate all possible combinations of tests which exhaustively test the given constraints.
3. If behavior in certain cases is unclear, you can ask on the forums
'''
from placeholders import *

# Convert a sentence which has either or to only the first choice.
# e.g we could either go to a movie or a hotel -> we could go to a movie.
# note: do not use intermediate lists (string.split), only use string functions
# assume words are separated by a single space. you can use control flow statements
# So sentence is of form <blah> either <something> or <somethingelse> and gets converted to <blah> <something>
# if it is not of the correct form, you just return the original sentence.
def prune_either_or(sentence):
    if sentence==None:
        return None
    s1=str(sentence)
    s=list(sentence)

    f=[]
    if "either" in s1:
     if (s1.index("either"))<2:
        return "".join(s);
    if 'either' in s1:
     if "or" in s1:
        l1=s1.index("either")
        for c,x in enumerate(s):
            if c < l1-1:

                f.append(x)
            else:
                break

        l2=s1.index("or")
        for c,x in enumerate(s):
            if c >(l1+5) and c <l2-1 :

                f.append(x)


        return "".join(f)
    else:
        return "".join(s)


def test_prune_either_or_student():
    assert "we could go to a movie"== prune_either_or("we could either go to a movie or a hotel")
    assert "we could go to a movie" == prune_either_or("we could go to a movie")
    assert None == prune_either_or(None)
    assert "either this or that" == prune_either_or("either this or that")
    assert "neither this or that" == prune_either_or("neither this or that")




# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_prune_either_or_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_prune_either_or(prune_either_or)
