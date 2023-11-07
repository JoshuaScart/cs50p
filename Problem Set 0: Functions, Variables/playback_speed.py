'''In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, 
replacing each space with ... (i.e., three periods).'''
# Ask the user for input
text = input("Insert your text here: ")

# Replace every space with three dots
newtext = text.replace(" ","...")

# Print the new text
print(newtext)
