#1 write a var to store the numbers into a list
#2 make sure the num are type int
#3 generate a loop to run hrough the list
#4 

user_entry = input("Enter a list of numbers (Please separate by spaces)")


user_entry_clean = user_entry.split()
print(user_entry_clean)

numbers_list = [int(num)for num in user_entry_clean]

print(numbers_list)

sum_of_num = None

count_positive = None

count_negative = None

count_zero = None


for num in numbers_list:
    if num > 0:
        count_positive + 1
        print(num + "is positive")
    elif num < 0:
        count_negative + 1
        print(num + "is negative")
    else:
        count_zero + 1
        print(num + "is zero")