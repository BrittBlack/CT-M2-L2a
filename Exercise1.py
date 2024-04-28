#Task 1: Code Correction
#
#
#
#
number = int(input("Enter a number: "))
#added int() because we are evaluating integers
if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
#deleted "number < 0" in else statement should be an elif
else:
    print("The number is negative.")