from user import *
import sqlite3
import sys

## class belongs to Dominic
## should interact with user 
## to link userID to the cart transaction
class Cart:

    ##constructor
    def __init__(self):        ## does the database have to be the same as the user database?
        self.cartDatabaseName = "cartDB.db"
        
    def cartMenu(self,user,cart): ## receving user class to track userID to cart
        while(1):
            print("Cart Information Menu:")
            print("0. Leave Cart Information")
            print("1. View Cart")
            print("2. Add To Cart")
            print("3. Remove From Cart")
            print("4. Check Out")
            
            cartOption = input("Enter your menu choice: ")

            ## Leave Cart Information
            if(option == "0"):
                break
    
            ## View Cart
            if(cartOption == "1"):
                cart.viewCart()   
                
            ## Add To Cart
            if(cartOption == "2"):
                cart.viewCart(self, ISBN, quantity)
                
            ## Remove From Cart
            if(cartOption == "3"):
                cart.viewCart(self,ISBN)
    
            ## Check Out
            if(cartOption == "4"):
                cart.viewCart(self,user.userID())


        
        print("Successfully Left Cart Information.")
        print()
        print("ending cart.py")
def viewCart(self): 
        cursor.execute(cart)
        print("end of the line buddy")

        
    
    def addToCart(ISBN, quantity): 
        ## add to database linked to cart
        a
    
    def removeFromCart(ISBN): 
        ## remove from database linked to cart
        a
    
    def checkOut(userID): 
        ## calls inventory to decrease stock
        ## calls orderHistory to make an order and fill out that order
        a
    

"""      TO DO------------------
        -link userID to cart
        -Prioritize completing Add and view cart
        -Prioritize completing remove from cart
        -finish checkout -----------------takes the longest so dont procrastinate 
"""

## while testing seperatly from main
def main():
        print("Welcome")
        user = User()
        temp = Cart()
        
        print("Testing for cartDB.db file")
        try:
            connection = sqlite3.connect(temp.cartDatabaseName)

        except:
            print("Failed database connection.")

            ## exits the program if unsuccessful
            sys.exit()
        cursor = connection.cursor()

        ## checks if the table cart already exists
        test = """SELECT (EXISTS(SELECT name FROM sqlite_master WHERE type='table' AND name='Cart'));"""

        ##if the table doesnt exist, creates a table
        if  cursor.execute(test)== 0:
            cart = """CREATE TABLE Cart (
                UserID varchar(7) NOT NULL,
                ISBN varchar(14) NOT NULL,
                Quantity int(3),
                FOREIGN KEY(UserID) REFERENCES User(UserID),
                FOREIGN KEY(ISBN) REFERENCES Inventory(ISBN)
            );"""
            cursor.execute(cart)

        ## calls the menu above
        temp.cartMenu(user,temp)
              
main()
