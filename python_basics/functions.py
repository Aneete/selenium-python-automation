#1️ Write a function to check if a number is positive, negative, or zero

def positve_negative_zero(num):
    if num>0:
        return "Positive"
    elif num<0:
        return "Negative"
    else:
        return "Zero"

number = int(input("enter the number"))
positve_negative_zero(number)

# Write a function that takes two numbers and returns the bigger one

def bigger_number(num1,num2):
    if num1>num2:
        print("num1 is bigger")
    elif num2>num1:
        print("num2 is bigger")
    else:
        print("both are same")

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
bigger_number(num1,num2)

#Write a function that prints numbers from 1 to n

def number_from_1ton(n):
    for i in range(1,n+1):
        print(i)

n= int(input("Enter the value of n"))
number_from_1ton(n)

# Write a function login_status(is_logged_in)
# If True → return "Login successful"
# Else → return "Login failed"

def login_status(is_logged_in):
    if is_logged_in:
        return"login successful"
    else:
        return"login failed"


login_status(True)
