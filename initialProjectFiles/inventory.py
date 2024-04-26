from user import *
import sqlite3
import sys

class Inventory:

    def __init__(self, databaseName="methods.db"):
        self.databaseName = databaseName

    def inventMenu(self): ## receving user class to track userID to cart
        while(True):
            print()
            print("Inventory Menu:")
            print("0. Leave Inventory")
            print("1. View Inventory")
            print("2. Search for Book")
            print("3. Decrease Quantity")
            
            inventChoice = input("What would you like to do (Type #)? ")
            
            match inventChoice:
                case "0":
                    break
                case "1":
                    self.viewInventory()
                    break
                case "2":
                    self.searchInventory()
                    break
                case "3":
                    self.decreaseStock()
                    break
                case _:
                    print("That is not a valid option. Try again.")
            
            break

    def viewInventory(self):
        try:
            connection = sqlite3.connect(self.databaseName)

        except:
            print("Failed database connection.")

            ## exits the program if unsuccessful
            sys.exit()
        cursor = connection.cursor()

        ## selects all information
        query = "SELECT * FROM Inventory"
        
        cursor.execute(query)
        print(cursor.fetchall())
        cursor.close()

    def searchInevntory(self):
        x = 1

    def descreaseStock(self):
        x = 1

        