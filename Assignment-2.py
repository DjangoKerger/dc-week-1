mystr = input("What is your string?")
mystr = mystr.casefold()
revstr = reversed(mystr)

if list(mystr) == list(revstr):
    print ("The string is a palindrome")
else: 
    print ("The string is not a palindrome")
