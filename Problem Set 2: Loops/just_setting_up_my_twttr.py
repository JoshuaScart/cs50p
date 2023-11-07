''' When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, 
implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase. '''

# Ask the user for input
txt = input("Input: ")

# Define a list of vowels for further use
vowels = ["a", "e", "i", "o", "u"]

# Iterate over each character in txt
for character in txt:
# If character is a vowel, print a empty space
  if character.lower() in vowels:
        print("", end="")
# If it isn't, print the character
  else:
        print(character, end="")
