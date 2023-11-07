'''In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. 
Assume that the user’s input will indeed be in camel case.'''

camel = input("camelCase: ")

# Iterate over each character in the input
for character in camel:
    if character.isupper(): 
        print("_" + character.lower(), end="") # If the character is uppercase, print a underscore and then the lowercase version of the character. Doesn't break the line.
    else:
        print(c, end="") # If the character isn't uppercase, it just print it. Also don't break the line, which is required for word formation.

print() # Print a new line since the other print functions didn't.
