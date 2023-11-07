''' In a file called extensions.py, implement a program that prompts the user for the name of a file and then 
outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes: 
.gif, .jpg, .jpeg, .png, .pdf, .txt, .zip. 
See developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types for common types. '''

# Ask the user for input
file = input("What's your file? ")

# "Lowercase" the input and remove any leading white spaces:
filef = file.lower().strip()

# Conditionals for every file extension:
if ".jpg" in filef or ".jpeg" in filef:
    print("image/jpeg")
elif ".gif" in filef:
    print("image/gif")
elif ".png" in filef:
    print("image/png")
elif ".pdf" in filef:
    print("application/pdf")
elif ".txt" in filef:
    print("text/plain")
elif ".zip" in filef:
    print("application/zip")
else:                          # If it's not an recognized file extension:
    print("application/octet-stream")
