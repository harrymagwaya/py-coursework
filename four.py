

# Write a python Write a Python program to compute the factorial of a given number using recursion. The program should:
# Define a function factorial(n) that returns the factorial of n.
# Take an integer input from the user.
# Compute the factorial of the entered number using the recursive function.
# Display the result.

num = int(input("Enter a number "))

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num -1)

    
print("result is ", factorial(num))


