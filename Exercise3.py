#Task 1: Leap Year Checker
#
#
#
year = int(input("Please enter a year: " ))
#every year that is divisible by '4' is a leap year

if year % 4 == 0 :
    print("This year is a leap year!")
if year % 100 == 0 :
    print("This is just another year.")
if year % 400 == 0 :
    print("This year is a leap year!")

#can't use elif or program would look for alternative instead original conditions
else:
    print("This is just another year.")