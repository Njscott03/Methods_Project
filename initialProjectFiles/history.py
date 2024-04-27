from user import *
from inventory import *
import sqlite3
import sys

class OrderHistory:
## belongs to Dakota
## should be interacting with the cart class
## to get basic order information
    
    def __init__(self):
        databaseName = "OrderDB.db"
        secondDatabaseName = "OrderItems.db"
        self.orderDatabaseName = databaseName
        self.secondDatabaseName = secondDatabaseName
    
  
    
    def viewHistory(userID):
        ##if either table doesnt exist make them
        a
        
    def viewOrder(userID, orderID): 
        a
        
    def createOrder(userID, quantity, cost, date):
        a
        
    def addOrderItems(userID, orderID):
        a

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
                ISBN = input("What is the ISBN:")
                quantity = input("What is the quantity:")
                cart.addToCart(ISBN, quantity,userID)
                
            ## Create Order
            if(historyOption == "3"):
                ISBN = input("What is the ISBN:")
                quantity = input("What is the quantity you want to remove:")

                cart.removeFromCart(ISBN,userID,quantity)
    
            ## Add to Order
            if(historyOption == "4"):
                cart.checkOut(userID)


        
        print("Successfully Left Cart Information.")
        print()
        print("ending history.py")


def main():
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

                
        history.historyMenu(userID,inventory,history)

main()
