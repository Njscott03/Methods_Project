from user import *
from cart import *
from inventory import *
import sqlite3
import sys

class OrderHistory:
## belongs to Dakota
## should be interacting with the cart class
## to get basic order information
    
    def __init__(self, databaseName = "methods.db"):
        self.orderDatabaseName = databaseName
    
  
        ## table of orders
    def viewHistory(self,userID):
        ##if either table doesnt exist make them
        
        try:
            connection = sqlite3.connect(self.orderDatabaseName)

        except:
            print("Failed database connection.")

            ## exits the program if unsuccessful
            sys.exit()
        cursor = connection.cursor()

        orderID = input("Input Order ID:")
        ## selects all information
        query = "SELECT ItemNumber,Cost,Date FROM Orders WHERE UserID ='" + userID + "'"
        print("Orders (ItemNumber, Cost, Date):")
        
        cursor.execute(query)
        print(cursor.fetchall()) ## i want to format the print...but it seems like an ungodly amount of work
        cursor.close()


        ## table of items
    def viewOrder(self,userID, orderID): 
        a = 1
        ##calls some function from inventory to display orderItems
        
    def createOrder(self,userID, quantity, cost, date):
        a = 1
        
    def addOrderItems(self, userID, orderID):
        a = 1


    def historyMenu(self,userID,inventory,history):
        print("inside gistoa")
        while(1):
            print()
            print("Cart Information Menu:")
            print("0. Leave History Information")
            print("1. View History")
            print("2. View Order")
            print("3. Create Order")
            print("4. Add to Order")

            ## userID = user.userID()
            userID = "123A567" ## this is purely a random ID that
                               ## wll be removed after User works
            
           
            historyOption = input("Enter your menu choice: ")

            ## Leave Cart Information
            if(historyOption == "0"):
                break
    
            ## View History
            if(historyOption == "1"):
                history.viewHistory(userID)   
                
            ## View Order
            if(historyOption == "2"):
                history.viewOrder(userID)
                
            ## Create Order
            if(historyOption == "3"):
                ISBN = input("What is the ISBN:")
                quantity = input("What is the quantity you want to remove:")

                ## Cart.removeFromCart(ISBN,userID,quantity)
    
            ## Add to Order
            if(historyOption == "4"):
                a = 1


        
        print("Successfully Left Cart Information.")
        print()
        print("ending history.py")


""" TO DO--------------------------------------------
-change how view order works
-make createOrder
-make addOrderItems
"""
def main(self):
        print("Welcome")

        ## userID = user.userID()
        userID = "211B" ##should be replaced when working in tandem with user

        ## test one
        print("Testing for methods.db file")
        try:
            connection = sqlite3.connect(self.orderDatabaseName)

        except:
            print("Failed database connection.")

                ## exits the program if unsuccessful
            sys.exit()
        cursor = connection.cursor()

            ## checks if the table cart already exists
        test = "SELECT (EXISTS(SELECT name FROM sqlite_master WHERE type='table' AND name='Orders'));"

        cursor.execute(test)
            
            ##if the table doesnt exist, creates a table
        if  cursor.fetchall()== [(0,)]:
            print("\nCreating Orders table...")
            
            query = """CREATE TABLE Orders (
                OrderNumber varchar(6) NOT NULL,
                UserID varchar(7) NOT NULL,
                ItemNumber int(5),
                Cost varchar(10),
                Date varchar(25),
                PRIMARY KEY(OrderNumber),
                FOREIGN KEY(UserID) REFERENCES User(UserID)
            );"""
            
            cursor.execute(query)
            print("Finished creating Orders table.")

            print("\nCreating OrderItems table...")
            order = """CREATE TABLE OrderItems (
                OrderNumber varchar(6) NOT NULL,
                ISBN varchar(14) NOT NULL,
                Quantity int(3),
                FOREIGN KEY(OrderNumber) REFERENCES Orders(OrderNumber),
                FOREIGN KEY(ISBN) REFERENCES Inventory(ISBN)
            );"""

            cursor.execute(order)
            
            connection.commit()
            ## shows changes
            
        cursor.close()
        print("\n--------------------------------------------")

                
        ## history.historyMenu(userID,inventory,history)
