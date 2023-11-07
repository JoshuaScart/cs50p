''' In the United States, it’s customary to leave a tip for your server after dining in a restaurant, typically an amount 
equal to 15% or more of your meal’s cost. Not to worry, though, we’ve written a tip calculator for you, below!'''

# I didn't insert it here because it'd make the file polluted!

''' Well, we’ve written most of a tip calculator for you. Unfortunately, we didn’t have time to implement two functions:

dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit), remove the leading $, 
and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.

percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit), remove the trailing %, 
and return the percentage as a float. For instance, given 15% as input, it should return 0.15.

Assume that the user will input values in the expected formats. '''


# Define the main function, that will ask for two inputs calling the conversion functions, multiply them and then print the result
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# Remove the dollar sign and them transform the number into a float
def dollars_to_float(d):
    d = float(d.replace("$",""))
    return d

# Remove the percentage sign and them transofrm the number into a float
def percent_to_float(p):
    p = float(p.replace("%",""))/100
    return p
  
# Calls the main function 
main()
