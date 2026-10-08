op = 0 
print("Hello user, please log into the system")

username = input("Username:")

while op < 5:
    password = input("Password:")

    if password == "test100":
        print("You have successfuly logged in")

    else:
        print("The password is incorrect try again \n ")
        op = op + 1 

print("you have reached the maximum attempts to log in")