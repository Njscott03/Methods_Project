from user import *
from history import *
from inventory import *
import sqlite3
import sys

## class belongs to Dominic
## should interact with user 
## to link userID to the cart transaction
class Cart:

    ##constructor
    def __init__(self):        
        self.databaseName = "Methods.db"


        ## uses initialized classes to call their 
    def cartMenu(self,user,history,inventory): ## receving user class to track userID to cart
        
        print("Testing for the database file...")
        try:
            connection = sqlite3.connect(self.databaseName)

        except:
            print("Failed database connection.")

            ## exits the program if unsuccessful
            sys.exit()
        cursor = connection.cursor()

        ## checks if the table cart already exists
        test = "SELECT (EXISTS(SELECT name FROM sqlite_master WHERE type='table' AND name='Cart'));"

        cursor.execute(test)
        
        ##if the table doesnt exist, creates a table
        if  cursor.fetchone()== None:   ##cursor.execute(test)
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
        
        
        

        
        while(1):
            print()
            print("Cart Information Menu:")
            print("0. Leave Cart Information")
            print("1. View Cart")
            print("2. Add To Cart")
            print("3. Remove From Cart")
            print("4. Check Out")
            
            userID = user.getUserID()
            cartOption = input("Enter your menu choice: ")
            
            ## Leave Cart Information
            if(cartOption == "0"):
                break
    
            ## View Cart
            if(cartOption == "1"):
                self.viewCart(userID)   
                
            ## Add To Cart
            if(cartOption == "2"):
                ISBN = input("What is the ISBN:")
                quantity = input("What is the quantity:")
                self.addToCart(ISBN, quantity,userID)
                
            ## Remove From Cart
            if(cartOption == "3"):
                ISBN = input("What is the ISBN:")
                self.removeFromCart(ISBN,userID)
    
            ## Check Out
            if(cartOption == "4"):
                self.checkOut(userID,history,inventory)


        
        print("Successfully Exited Cart Information.")
        print()


    def viewCart(self,userID):
        #view a database linked to cart
        
        try:
            connection = sqlite3.connect(self.databaseName)

        except:
            print("Failed database connection.")

            ## exits the program if unsuccessful
            sys.exit()
        cursor = connection.cursor()


        ## selects all a tuple of Cart's ISBN
        query = "SELECT ISBN FROM Cart WHERE Cart.UserID ='" + userID + "'"
        cursor.execute(query)
        cartIsbnTuple = cursor.fetchall()

        ## selects all a tuple of Inventory's ISBN
        query = "SELECT ISBN FROM Inventory"
        cursor.execute(query)
        InventoryIsbnTuple = cursor.fetchall()


        ## selects all inventory information and Cart information
        ## and displays the user's items
        query = "SELECT Inventory.ISBN, Inventory.Title,Inventory.Author,Inventory.Genre,Inventory.Price,Inventory.ReleaseDate, Inventory.Stock, Inventory.Pages, Cart.Quantity,Cart.UserID FROM Inventory, Cart  WHERE Inventory.ISBN = Cart.ISBN AND '" + userID + "'= Cart.UserID"
        cursor.execute(query)
        view = cursor.fetchall()

        print()
        print("Valid Cart Items:")
        print("[ISBN, Title, Author, Genre, Price, ReleaseDate, Stock, Pages, Quantity, UserID]")
        print()
        
        print("---------------------------------")
        for item in view:
            print(item)
            print("---------------------------------")

        
        cursor.close()
        



        
    def addToCart(self,ISBN,quantity,userID):
        ## add to a database linked to cart
        
        try:
            connection = sqlite3.connect(self.databaseName)

        except:
            print("Failed database connection.")

            ## exits the program if unsuccessful
            sys.exit()
        cursor = connection.cursor()
        
         ## test valid ISBN
        query = "SELECT ISBN FROM Inventory WHERE Stock > 0"
        cursor.execute(query)
        InventoryIsbnTuple = cursor.fetchall()
        
        isValid = False
        for item in InventoryIsbnTuple:
            if item == (ISBN,):
                isValid = True
        if isValid == False:
            print("The entered ISBN is invalid please reference inventory to make sure the item is in stock")
            return

        ## test valid quantity
        query = "Select Stock FROM Inventory WHERE ISBN ='" + ISBN + "'"
        cursor.execute(query)
        stock = cursor.fetchone()
        
        if stock[0] - int(quantity) < 0:
            print("Your quantity exceeds the current stock.")
            return
        
    
        ## checks if the item exists in the table
        test = "SELECT UserID FROM Cart WHERE userID = '" + userID + "' AND ISBN = '" + ISBN + "';"

        cursor.execute(test)
        results = cursor.fetchone()

        ## checking if is inside the table
        if  results == None:

            ## Inserts book into table
            query = "INSERT INTO Cart (UserID, ISBN, Quantity) VALUES ('" + userID +"','" + ISBN + "','" + quantity + "')"
            
        else:
            
            ## adding user input quantity to table quantity
            query = "Select Quantity FROM Cart WHERE ISBN ='" + ISBN + "'" + "AND UserID ='" + userID + "'"
            cursor.execute(query)
            cartQuantity = cursor.fetchone()
        
            if stock[0] - (int(quantity) + int(cartQuantity[0])) < 1:
                print("Your total quantity exceeds the current stock.")
                return
            
            query = "UPDATE Cart SET Quantity = Quantity +" + quantity + " WHERE UserID = '" + userID + "' AND ISBN = '" + ISBN + "';"
            

        print()
        cursor.execute(query)
        connection.commit()
        cursor.close()

                
    
    def removeFromCart(self,ISBN,userID): 
        
        try:
            connection = sqlite3.connect(self.databaseName)

        except:
            print("Failed database connection.")

            ## exits the program if unsuccessful
            sys.exit()
        cursor = connection.cursor()


        query = "SELECT Quantity FROM Cart Where ISBN ='" + ISBN + "' AND UserID ='" + userID + "'"
        cursor.execute(query)
            
        Quantity = cursor.fetchone()
        quantity = str(Quantity[0])


        
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
    
    def checkOut(self,userID,history,inventory): 
        ## calls orderHistory to make an order and fill out that order
        try:
            connection = sqlite3.connect(self.databaseName)
            
        except:
            print("Failed database connection.")

            ## exits the program if unsuccessful
            sys.exit()
        cursor = connection.cursor()
            
        date = "4/29/24"
        orderID = history.createOrder(userID,0,0,date)

        query = "SELECT ISBN FROM Cart WHERE userID ='" + userID + "'"
        cursor.execute(query)
        cartISBNtuple = cursor.fetchall()
        
        ##fix loop, using a cursor.execute(query) where
        for ISBNs in cartISBNtuple:
            currentISBN = ISBNs[0]
            query = "SELECT Quantity FROM Cart Where ISBN ='" + currentISBN + "' AND UserID ='" + userID + "'"
            cursor.execute(query)
            
            Quantity = cursor.fetchone()
            quantity = Quantity[0]
            strQuantity = str(quantity)
            
            
            history.addOrderItems(userID,orderID,quantity)
            inventory.decreaseStock(currentISBN, quantity)

            ## passes quantity as a string because it is concatonated
            ## in an sql query
            self.removeFromCart(currentISBN,userID,strQuantity)

