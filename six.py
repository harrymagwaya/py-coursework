
# Write a Python program using SET to create an Email Book application that allows the following functionalities:
# Add: Add a new email address to the email book (if it does not already exist).
# Search: Search for an email address to see if it exists in the email book.
# Remove: Remove an email address from the email book.
# List: Display all email addresses in the email book.
# Exit: Exit the program.

email_set = set()

while True:
    print("******Email book*******")
    print("1. Add email")
    print("2. Search for email")
    print("3. Remove an email")
    print("4. List all emails")
    print("5. Exit")

    option = int(input("Enter a number for an option: "))
    if option ==1:
        email= input("Enter an email address")
        if email in email_set:
            print(email, "exists")
        else:
            email_set.add(email)
    elif option ==2:
        email = input("Enter an email address: ")
        if email in email_set:
            print(email, "found")
        else:
            print(email, "doesnt exist")
    elif option ==3:
        email= input("Enter an email address")
        if email in email_set:
            email_set.remove(email)
        else:
            print(email, "doesnt exist")
    elif option ==4:
        for i in email_set:
            print(i)
    elif option ==5:
        break


