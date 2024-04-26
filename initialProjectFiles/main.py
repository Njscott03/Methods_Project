from user import *
from cart import *
from inventory import *
from history import *

user = User()
cart = Cart()
inventory = Inventory()
history = OrderHistory()

## COMPLETE initial pre-login menu
def initialMenu():
    ## objects for the classes

    ## initial menu
    while(1):
        print("Pre-Login Menu:")
        print("0. Login")
        print("1. Create Account")
        print("2. Exit Program")
        initial = input("Enter your menu choice: ")
        print()

        if(initial == "0"):
            user.login()

        elif(initial == "1"):
            user.createAccount()

        ## exit program
        elif(initial == "2"):
            print("Good-bye!")
            break

        ## incorrect menu option
        else:
            print("That's not a menu option. Please try again.")

        print()

        ## checks status after one menu loop...
        ## goes into main menu if applicable
        if(user.getLoggedIn()):
            mainMenu(user, cart, inventory, history)


## incomplete main menu...
def mainMenu(user, cart, inventory, history):
    while(user.getLoggedIn()):
        print("Main Menu:")
        print("0. Logout")
        print("1. View Account Information")
        print("2. Inventory Information")
        print("3. Cart Information")
        print("4. Order Information")
        option = input("Enter your menu choice: ")
        print()

        ## logging out
        if(option == "0"):
            user.logout()

            print("Successful logout.")

        ## View Account Information
        elif(option == "1"):
            user.viewAccountInformation()

        ## Inventory Information
        elif(option == "2"):
            inventory.inventMenu()
            
        ## Cart Information
        elif(option == "3"):
            cart.cartMenu(user)    

        ## Order Information
        elif(option == "4"):
            history.orderMenu(user)    
               
        ## incorrect menu option
        else:
            print("That's not a menu option. Please try again.")

        print()




def main():
    print("Welcome to the online bookstore!\n")

    initialMenu()

main()
