''' In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, 
outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No. '''

# Prompts the user for the answer:
answer = input("What's the answer to The Great Question Of Life?")

# Makes the program case-insensitive by 'lowering' any input:
answer = answer.lower()

# Transform "forty-two" and "forty two" into "fortytwo":
answer = answer.replace("-","").replace(" ","")


if answerc=="fortytwo" or answerc=="42": # If the answer is correct, print "Yes."
    print("Yes.")
else:                                    # If the answer is incorrect, print "No."
    print("No.")
