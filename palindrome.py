String = input("Enter a String: ")
Character = ""

for i in String:
    Character = i + Character 
if Character == String: 
    print("It is a Palindrome")
else:
    print("It is not a Palindrome") 
