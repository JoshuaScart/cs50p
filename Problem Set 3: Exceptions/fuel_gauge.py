'''Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. 
If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.'''

while True:
    try:
        # Ask the user for input and split it using the slash as reference
        x, y = input("Insert a fraction: ").split("/")
      
        # Transform x and y into integers
        x = int(x)
        y = int(y)
      
        # Transform the fraction into percentage
        dec = x / y * 100 
      
        if x >= 99 and y >= 99: # If the tank is full or almost full, print "F"
            print("F")
            break
        elif x <= 1 and y == 100: # If the tank is empty or almost empty, print "E"
            print("E")
            break
        elif x < y or y != 0: # If x is smaller than y or y isn't 0, print the percentage befitting the fuel gauge
            print(f"{dec:.0f}%")
            break
        else:                 # If x is bigger than y or y is 0, print a error message
            print("Invalid fraction. Please make sure x < y and y is not zero.")
          
    except (ValueError, ZeroDivisionError, AttributeError):  # If the program encounter any errors, print a message.
        print("Something's wrong.")
