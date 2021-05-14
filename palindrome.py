#Asks the user for string, determines if it is a palidrome or not

def check(str):

    #str = str(input("Enter a string: "))

    for i in range(0,int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
        return True

#while True:

        
        #s = str(input("Enter a string: "))
        #p = check(s)

        #if check(s) == False:
           # print("Not a palindrome")
       # else:
          #  print("Is a palindrome")