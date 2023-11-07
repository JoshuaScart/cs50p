''' In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. 
Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that 
isn’t an accepted denomination.'''

amount = 0

# Infinite loop to simulate a vending machine
while True:
    print(f"Amount Due: {50 - amount}")
    
    # Ask user input for inserting coins
    coin = int(input("Insert Coin: "))

    # Check if the value is valid
    if coin != 5 and coin != 10 and coin != 25:
        continue
    else:
        amount += coin
    
    # Break the loop if the amount due is met or exceeded
    if amount >= 50:
        break

# Print the change
print(f"Change Owed: {amount - 50}")
