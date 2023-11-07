''' In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then 
calculates and outputs the result as a floating-point value formatted to one decimal place. 
Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer

For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0. '''


# Asks for the user input:
cal = input("Insert your calculation here: ")

# Split the string into a list using the whitespaces:
cals = cal.split(" ")

# Makes each element of the list an operator of the calculaiton
num1 = float(cals[0])
op = cals[1]
num2 = float(cals[2])

if op == "+":
    print(num1 + num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
elif op == "-":
    print(num1 - num2)
