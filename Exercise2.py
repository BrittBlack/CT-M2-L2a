#Task 1: Identify the Greatest
#
#
#
#
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))



large = num1
   
if num2 > num1:
    large = num2
elif num3 > num1:
    large = num3
else: 
    print("The largest number is:", large )

#
#
#
#
#Task 2: Identify the Smallest

small = num1
   
if num2 < num3:
    small = num1
elif num3 < num1:
    small = num3
else:
    print("The smallest number is:", small)

#
#
#
#
#Task 3: Equality Check

if num1 == num2 == num3:
    print("All numbers are equal.")
elif num1 == num2:
    print(f"{num1} is equal to {num2}." "The largest number is:", large, "The smallest number is:", small)
elif num2 == num3:
    print(f"{num2} is equal to {num3}.""The largest number is:", large, "The smallest number is:", small)
elif num1 == num3:
    print(f"{num1} is equal to {num3}.""The largest number is:", large, "The smallest number is:", small)
else:
    print("All numbers are not equal.")
