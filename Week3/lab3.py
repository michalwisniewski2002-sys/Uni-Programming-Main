print("*******WELCOME TO OUR BANK*******")

user_name=input(("Please enter your name"))

balance = 1000
op=True

while op == True: #student completes while loop

    print("\n\n Choose 1 for Deposit \n Choose 2 for Withdraw \n Choose 3 for Check Balance \n Choose Q or q to Exit:")
    choice = input("Please choose transactions:")

    if choice == "1": #user chooses 'deposit'
         #student completes while loop
        print("Thank you for choosing to deposit")
        balance = balance + int(input("How much would you like to deposit:"))

    elif choice == "2":
       #student completes while loop
       print("Thank you for choosing to withdraw")
       balance = balance - int(input("How much would you like to deposit:"))

        
    elif choice=="3":
        #student does this part too
      pass

    elif choice.upper == "Q":#user chooses 'exit'
        
        print("""
    -------------------------------------
   | Thanks for choosing us as your bank |
   | Visit us again!                     |
    -------------------------------------
        """)
        op= False #student does this part too
    else:
        print("Wrong transaction! Try again.")

   