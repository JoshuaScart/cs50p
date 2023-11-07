'''In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) 
and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.'''

# Ask the user for input
mass = input("What's the mass in kg?")

# "Transform" mass into Joules
energy = int(mass)*300000000**2

# Print the result
print(f"E={energy}")
