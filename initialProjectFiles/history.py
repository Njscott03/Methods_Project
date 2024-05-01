from user import *
from inventory import *
import random
import sqlite3
import sys


class OrderHistory:
## belongs to Dakota
## should be interacting with the cart class
## to get basic order information
    
    def __init__(self):
        self.orderDatabaseName = "methods.db"
        
    
  
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
        query = "SELECT * FROM Orders WHERE OrderNumber ='" + orderID + "'"
        print("Orders (ItemNumber, Cost, Date):")
        
        cursor.execute(query)
        results = cursor.fetchall()
        
        print(results) ## i want to format the print...but it seems like an ungodly amount of work
        cursor.close()


        ## table of items
    def viewOrder(self,userID, orderID): 
        print("inside viewOrder")
        ##calls some function from inventory to display orderItems

        
    def createOrder(self,userID, quantity, cost, date):
        print("inside createOrder")
        try:
            connection = sqlite3.connect(self.orderDatabaseName)

        except:
            print("Failed database connection.")

            ## exits the program if unsuccessful
            sys.exit()
        cursor = connection.cursor()
        
        orderNum = random.randint(100000, 999999)
        query = "SELECT OrderNumber FROM Orders WHERE userID='" + userID + "'"
        cursor.execute(query)
        OrderNumTuple = cursor.fetchall()


        ## what are the odds the order number is the same for one userID after regeneration
        for item in OrderNumTuple:
            if(orderNum,) == item:
                orderNum = random.randint(100000, 999999)
        
        query = "INSERT INTO Orders (OrderNumber, UserID, itemNumber) VALUES (?,?,?)"
           
        ## definitly unfinished. i wanted to have cart play well with the function but....not happening
        

        ## grab current date
        
    def addOrderItems(self,orderID,ISBN, quantity):
        print("inside addOrderItems")
        print(ISBN)
        ## would call a query to add ISBN and Quantity to OrderItems, linked by orderNumber



    def historyMenu(self,userID,inventory):
        print("Welcome")
        user = User()
        history = OrderHistory()
        inventory = Inventory()

        ## userID = user.userID()
        userID = "211B" ##should be replaced when working in tandem with user

        ## test one
        print("Testing for orders.db file")
        try:
            connection = sqlite3.connect(history.orderDatabaseName)

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






        print("inside History Menu")
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
                history.viewOrder(userID, orderID)
                
            ## Create Order
            if(historyOption == "3"):
                
                cart.createOrder(userID,quantity,cost,date)
    
            ## Add to Order
            if(historyOption == "4"):
                cart.checkOut(userID)


        
        print("Successfully Left Cart Information.")
        print()
        print("ending history.py")


""" TO DO--------------------------------------------
-change how view order works
-make createOrder
-make addOrderItems
"""

history = OrderHistory()
inventory = Inventory()
##history.historyMenu("15-5444",inventory)

