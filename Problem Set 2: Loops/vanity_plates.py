'''In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

    “All vanity plates must start with at least two letters.”
    “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    “No periods, spaces, or punctuation marks are allowed.”

In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input
will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. 
You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement). '''


# Defines the main function that ask the user for input and calls for the is_valid function in order to check if it is valid
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(p):
    if len(p) < 2 or len(p) > 6:  # Check if the lenght of the plate is smaller than 2 or bigger than 6
        return False
    if not p[0:2].isalpha():      # Check if the first two characters are letters
        return False

  
    i = 0                         # The while loop will continue to iterate as long as i is less than the length of the plate string. This ensures that the entire plate is checked
    while i < len(p):
        if p[i].isnumeric():
            if p[i] == "0":       # Check if the first number is zero
                return False
            else:
                break
        i += 1                    # Adds 1 to "i" in order to check every character of the plate

  
    for _ in p:                   
        if not _.isalnum():       # Return false if any character isn't a number or a letter
            return False

  # If the last, or second to last, or third to last, or all three of the characters are letters and the plate has a number before them, return false
    if p[-1].isalpha() or p[-2].isalpha() or (p[-1].isalpha() and p[-2].isalpha()) or (p[-1].isalpha() and p[-2].isalpha() and p[-3].isalpha()):
        for a in p:
            if a.isnumeric():
                return False
 # If the plate passes in all tests, return true
    return True


main()
