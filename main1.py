# #Write a Python program
# that performs the following operations
# on a list of numbers: -Input the List of Numbers: The
# program should take a list of numbers (integers) as input from the user. The user
# - Classify Numbers: For each number in the list, classify
# will input the numbers separated by spaces.
# it into one of the following categories: Positive: The number is
# greater than zero. Negative: The number is less than zero. Zero: The number is exactly zero. - Even or Odd Classification:
# For each number, determine whether
# is even or odd: Even: A number that
# number that is not divisible by 2. - Calculate the Sum and
# is divisible by 2 (i.e., number % 2
# 0). Odd: A
# Average: Calculate the sum of all the numbers in the list. Calculate
# the average of the numbers in the list by dividing the sum by the total number of numbers. - Count the Numbers: Count how
# many numbers are positive, negative, and zero.

user_entry = input("Enter a list of numbers (Please separate by spaces):  ")
user_entry_clean = user_entry.split()
print(user_entry_clean)

numbers_list = [int(num)for num in user_entry_clean]
print(numbers_list)

sum_of_num = 0

average_of_num = None

count_positive = 0

count_negative = 0

count_zero = 0

num_of_items = len(numbers_list)

for num in numbers_list:
    if num > 0:
        count_positive  = count_positive + 1
        print("Positive: ", num , "is positive")
        if num %2 == 0:
            print(num, "is an even number")
        else:
            print(num, "is an odd number")
    elif num < 0:
        count_negative = count_negative + 1
        print("Negative: ", num , "is less than zero")
        if num % 2 == 0:
            print(num, "is an even number")
        else:
            print(num, "is an odd number")
    else:
        count_zero = count_zero + 1
        print(num , "is exactly zero")
    sum_of_num = sum_of_num + num
    average_of_num = sum_of_num / num_of_items

print("count positive is ", count_positive)
print("count positive is ", count_negative)
print("count positive is ", count_zero)

print("Average: ", average_of_num)
print("Sum: ", sum_of_num)
