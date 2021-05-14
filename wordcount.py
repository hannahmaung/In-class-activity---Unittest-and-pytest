#Program that counts the amount of words in the program 

def count(string):
    counter = 1

    #removes spaces
    new = string.strip()

    for i in new:
    #if there is a space, increment count
        if i == " ":
            counter = counter + 1
    #returns word count in each sentence
    return counter
 
