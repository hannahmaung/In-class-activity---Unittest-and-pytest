#Unit test for word count program 
import unittest 
import wordcount

class testCase(unittest.TestCase):

    def setup(self):
        self.wordcount = wordcount()
    #This test should pass because the input is only one word and the output is set to one 
    def test1(self):
        self.assertEqual(wordcount.count("hannah"),(1))
    #This test should pass because there are 3 words in the input and the output is set to 3
    def test2(self):
        self.assertEqual(wordcount.count("hannah is awesome"), (3))
    #This test should fail because there are 4 words in the input and the output is set to 5
    def test3(self):
        self.assertEqual(wordcount.count("CS is really hard"),(5))

if __name__ == "__main__":
    unittest.main()