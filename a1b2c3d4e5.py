string=input("Enter a string:")

number=""
result=""
previous=""

for character in string:
    if 'a' <= character <= 'z' or 'A' <= character <= 'Z':
        if number != "":
            result = result + previous *int(number) 
            number =""
        previous = character 
    else:
        number = number + character 

if number != "":
    result = result + previous * int(number)

print(result)
