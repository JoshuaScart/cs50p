'''In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. 
If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. 
And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.
Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, 
to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).'''

# Defines the main function, where it will ask for input, call for the time conversion function and name a meal based on the hour
def main():
    time1 = input("What time is it? ")
    time2 = convert(time1)
    if 7.0 <= time2 <= 8.0:
        print("breakfast time")
    elif 12.0 <= time2 <= 13.0:
        print("lunch time")
    elif 18.0 <= time2 <= 19.0:
        print("dinner time")

# Converts input time in 12-hour format to 24-hour format and returns it as a decimal hour 
def convert(time):
    if time[-1].isdigit() or time.endswith("a.m."):
        time5 = time.replace("a.m.", "")
        hours1, minutes1 = time5.split(":")
        hours = int(hours1)
        minutes = int(minutes1)
        th = hours + minutes / 60

    elif time.endswith("p.m."):
        time5 = time.replace(" p.m.", "")
        hours1, minutes1 = time5.split(":")
        hours = int(hours1)
        minutes = int(minutes1)
        th = (hours + minutes / 60) + 12
    return th

# Call for the main function
if __name__ == "__main__":
    main()
