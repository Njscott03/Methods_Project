from user import *
import sqlite3
import sys

## class belongs to Dominic
## should interact with user 
## to link userID to the cart transaction
class Cart:

    ##constructor
    def __init__(self):        
        self.cartDatabaseName = "cartDB.db"
        
    def cartMenu(self,user,cart): ## receving user class to track userID to cart
        while(1):
            print()
            print("Cart Information Menu:")
            print("0. Leave Cart Information")
            print("1. View Cart")
            print("2. Add To Cart")
            print("3. Remove From Cart")
            print("4. Check Out")
            
            ## userID = user.userID()
            userID = "123A567" ## this is a non changing ID and
                               ## wll be removed after User works
            
            cartOption = input("Enter your menu choice: ")
            
            ## Leave Cart Information
            if(option == "0"):
                break
    
            ## View Cart
            if(cartOption == "1"):
                cart.viewCart(userID)   
                
            ## Add To Cart
            if(cartOption == "2"):
                ISBN = input("What is the ISBN:")
                quantity = input("What is the quantity:")
                cart.addToCart(ISBN, quantity,userID)
                
            ## Remove From Cart
            if(cartOption == "3"):
                ISBN = input("What is the ISBN:")
                quantity = input("What is the quantity you want to remove:")

                cart.removeFromCart(ISBN,userID)
    
            ## Check Out
            if(cartOption == "4"):
                cart.checkOut(userID)


        
        print("Successfully Left Cart Information.")
        print()
        print("ending cart.py")


    def viewCart(self,userID):
        #view a database linked to cart
        
        try:
            connection = sqlite3.connect(self.cartDatabaseName)

        except:
            print("Failed database connection.")

            ## exits the program if unsuccessful
            sys.exit()
        cursor = connection.cursor()

        ## selects all information
        query = "SELECT ISBN,Quantity FROM Cart WHERE UserID ='" + userID + "'"
        print("Cart Items (ISBN,Quantity):")
        
        cursor.execute(query)
        print(cursor.fetchall()) ## i want to format the print...but it seems like an ungodly amount of work
        cursor.close()

        
    def addToCart(self,ISBN,quantity,userID):
        ## add to a database linked to cart
        
        try:
            connection = sqlite3.connect(self.cartDatabaseName)

        except:
            print("Failed database connection.")

            ## exits the program if unsuccessful
            sys.exit()
        cursor = connection.cursor()

        ## checks if the item exists in the table
        test = "SELECT UserID FROM Cart WHERE userID = '" + userID + "' AND ISBN = '" + ISBN + "';"

        cursor.execute(test)
        results = cursor.fetchone()
        print(results)

        
         
        cursor.execute(test)
        ## checking if is inside the table
        if  results == None:

            ## Inserts book into table
            query = "INSERT INTO Cart (UserID, ISBN, Quantity) VALUES ('" + userID +"','" + ISBN + "','" + quantity + "')"
            print(query)
            
        else:
            
            ## adding user input quantity to table quantity
            query = "UPDATE Cart SET Quantity = Quantity +" + quantity + " WHERE UserID = '" + userID + "' AND ISBN = '" + ISBN + "';"
            print(query)

        cursor.execute(query)
        connection.commit()
        cursor.close()
        
                
                
    
    def removeFromCart(self,ISBN,userID): 
        ## remove from a database linked to cart
        
        try:
            connection = sqlite3.connect(self.cartDatabaseName)

        except:
            print("Failed database connection.")

            ## exits the program if unsuccessful
            sys.exit()
        cursor = connection.cursor()

        ## checks if the item exists in the table
        test = "SELECT UserID FROM Cart WHERE userID = '" + userID + "' AND ISBN = '" + ISBN + "';"

        cursor.execute(test)
        results = cursor.fetchone()
        print(results)

        cursor.execute(test)
        ## checking if is inside the table
        if  results == None:
        ## item doesn't exist
            
            print("That ISBN is not in your cart")
            
        else:
        ##item exists
            
            ## removing user input quantity from table quantity
            query = "UPDATE Cart SET Quantity = Quantity -" + quantity + " WHERE UserID = '" + userID + "' AND ISBN = '" + ISBN + "';"
            cursor.execute(query)

            ## removes any items w/  < 1 quantity
            query = "Delete FROM Cart Where userID = '"+ userID + "' AND Quantity < 1"
            cursor.execute(query)
            connection.commit()
        
        cursor.close()
    
    def checkOut(userID): 
        ## calls inventory to decrease stock
        ## calls orderHistory to make an order and fill out that order
        ## delete the entire cart contents relating to a specific user 
        a
    

"""      TO DO------------------
        -fix cart initialization
        -add a delete from table when quantity = 0
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
        test = "SELECT (EXISTS(SELECT name FROM sqlite_master WHERE type='table' AND name='Cart'));"

        cursor.execute(test)
        
        ##if the table doesnt exist, creates a table
        if  cursor.fetchall()== [(0,)]:   ##cursor.execute(test)
            query = """CREATE TABLE Cart (
                UserID varchar(7) NOT NULL,
                ISBN varchar(14) NOT NULL,
                Quantity int(3),
                FOREIGN KEY(UserID) REFERENCES User(UserID),
                FOREIGN KEY(ISBN) REFERENCES Inventory(ISBN)
            );"""
            cursor.execute(query)
           
            connection.commit()
            cursor.close()

        ## calls the menu above
        temp.cartMenu(user,temp)
              
main()
