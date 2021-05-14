#Pytest for Palindrome program

import pytest
import palindrome

#This test should pass because the input is a palindrome 
def test_1():
    input = "hannah"
    assert palindrome.check(input) == True

#This pass should pass because the input is not a palindrome and the output is set to False 
def test_2():
    input = "engineering"
    assert palindrome.check(input) == False

#This pass should fail because the input is not a palindrome and the output is set to True 
def test_3():
    input = "brandon"
    assert palindrome.check(input) == True  

if __name__ == "__main__":
    pytest.main()

