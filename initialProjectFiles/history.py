from user import *
from history import *
from inventory import *
import sqlite3
import sys

class OrderHistory:
## belongs to Dakota
## should be interacting with the cart class
## to get basic order information
    def OrderHistory(self):
        ## nothing needs to be initialized

def OrderHistory(databaseName):
    self.orderDatabaseName = databaseName
    
def viewHistory(userID):
    ##if either table doesnt exist make them

 



## order items table
print("\nCreating OrderItems table...")

order = """CREATE TABLE OrderItems (
    OrderNumber varchar(6) NOT NULL,
    ISBN varchar(14) NOT NULL,
    Quantity int(3),
    FOREIGN KEY(OrderNumber) REFERENCES Orders(OrderNumber),
    FOREIGN KEY(ISBN) REFERENCES Inventory(ISBN)
);"""

cursor.execute(order)
print("Finished creating OrderItems table.")
print("\nAdding OrderItems records...")

connection.commit()

    
def viewOrder(userID, orderID): 
    a
    
def createOrder(userID, quantity, cost, date):
    a
    
def addOrderItems(userID, orderID):
    a

def historyMenu(userID,inventory,order)

def main():
    print("Welcome")
    user = User()
    temp = orderHistory(orders)
    inventory = inventory()
    order = orderHistory()

    ## test one
    print("Testing for orders.db file")
    try:
        connection = sqlite3.connect(temp.cartDatabaseName)

    except:
        print("Failed database connection.")

            ## exits the program if unsuccessful
        sys.exit()
    cursor = connection.cursor()

        ## checks if the table cart already exists
    test = "SELECT (EXISTS(SELECT name FROM sqlite_master WHERE type='table' AND name='order'));"

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
        print("\nAdding Orders records...")
        
        
        connection.commit()
        ## shows changes
    cursor.close()
    print("\n--------------------------------------------")
    
    historyMenu(userID,inventory,history)


