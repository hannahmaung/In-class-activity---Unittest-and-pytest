#Unit test for palindrome program
import unittest 
import palindrome

class testCase(unittest.TestCase):

    def setup(self):
        self.palindrome = palindrome()
    #Test 1 is going to pass because it is a palindrome
    def test1(self):
        self.assertEqual(palindrome.check("hannah"),(True))
    #Test 2 is going to fail because input is not a palindrome and the result is set to True
    def test2(self):
        self.assertEqual(palindrome.check("coooool"), (True))
    #Test 3 is going to pass because the input is not a palindrome is the result is set to Flase
    def test3(self):
        self.assertEqual(palindrome.check("enginerring"),(False))

if __name__ == "__main__":
    unittest.main()