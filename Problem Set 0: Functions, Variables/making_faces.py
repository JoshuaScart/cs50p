'''In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 and any :( converted to 🙁. 
All other text should be returned unchanged.
Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, and prints the result. 
You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input. Be sure to call main at the bottom of your file.'''

# Define the main function, that will ask for input, call for the conversion function and print the converted text
def main():
    text = input("Insert text here: ")
    newtext = convert(text)
    print(newtext)

# Define the convert function, that will replace emoticons for emojis
def convert(t):
    t = t.replace(":)", "🙂")
    t = t.replace(":(", "🙁")
    return t

# Call the main functions
main()
