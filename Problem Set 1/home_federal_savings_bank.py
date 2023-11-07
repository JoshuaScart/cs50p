''' In a file called bank.py, implement a program that prompts the user for a greeting. 
If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. 
Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively. '''

# Ask the user for the input
answer=input("A customer arrives at you bank, how do you great him?")

# Lowercase the input and remove any leading whitespaces
answerf=answer.lower().strip()

if answerf.startswith("hello"): # If the answer starts with "hello", print "$0".
    print("$0")
elif answerf.startswith("h"):   # If the answer starts with "h", print "$20".
    print("$20")
else:													  # If the answer is anything except something that starts with an "h" or "hello" print "$100".
    print("$100")
