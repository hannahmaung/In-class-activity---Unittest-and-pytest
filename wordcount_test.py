#Pytest for Word Count program

import pytest
import wordcount 

#This test should pass because the input has 4 words and the output is set to 4
def test_1():
    input = "This class is fun"
    assert wordcount.count(input) == 4

#This pass should pass because the input has 5 words and the output is set to 5
def test_2():
    input = "My major is computer science"
    assert wordcount.count(input) == 5

#This pass should fail because the input has 1 word and the output is set to 0
def test_3():
    input = "hi"
    assert wordcount.count(input) == 0

if __name__ == "__main__":
    pytest.main()