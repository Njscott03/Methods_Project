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
            print("0. View Inventory")
            print("1. Search for Book")
            print("2. Decrease Quantity")
            print("3. Leave Inventory")
            print()
            
            inventChoice = input("What would you like to do (Type #)? ")
            print()
            
            match inventChoice:
                case "0":
                    self.viewInventory()
                case "1":
                    self.searchInventory()
                case "2":
                    ISBN = input("What ISBN would you like to decrease? ")
                    quantity = input("How many? ")

                    self.decreaseStock(ISBN, quantity)
                case "3":
                    break
                case _:
                    print("That is not a valid option. Try again.")
            

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
        result = cursor.fetchall()
        for x in range(len(result)):
            ISBN = result[x][0]
            title = result[x][1]
            author = result[x][2]
            genre = result[x][3]
            pages = result[x][4]
            releaseDate = result[x][5]
            price = result[x][6]
            stock = result[x][7]

            ## displays results
            print("ISBN:", ISBN)
            print("Title:", title)
            print("Author:", author)
            print("Genre:", genre)
            print("Pages:", pages)
            print("Release Date:", releaseDate)
            print("Price: $" + str(price))
            print("Stock:", stock, "\n")
        cursor.close()

    def searchInventory(self):
        bookTitle = input("What is the name of the book? ")
        print()
        try:
            connection = sqlite3.connect(self.databaseName)

        except:
            print("Failed database connection.")

            ## exits the program if unsuccessful
            sys.exit()
        cursor = connection.cursor()

        ## queries the title of the book and pulls all info
        query = "SELECT * FROM Inventory WHERE Title=?"
        data = (str(bookTitle),)
        cursor.execute(query, data)
        result = cursor.fetchall()
        if (len(result) == 0):
            print("There is no book with this name.")
        else:
            ISBN = result[0][0]
            title = result[0][1]
            author = result[0][2]
            genre = result[0][3]
            pages = result[0][4]
            releaseDate = result[0][5]
            price = result[0][6]
            stock = result[0][7]

            ## displays results
            print("ISBN:", ISBN)
            print("Title:", title)
            print("Author:", author)
            print("Genre:", genre)
            print("Pages:", pages)
            print("Release Date:", releaseDate)
            print("Price: $" + str(price))
            print("Stock:", stock)
        
        cursor.close()

    def decreaseStock(self, ISBN, quantity):
        try:
            connection = sqlite3.connect(self.databaseName)

        except:
            print("Failed database connection.")

            ## exits the program if unsuccessful
            sys.exit()
        cursor = connection.cursor()

        ## checks if the ISBN is in the inventory
        query = "SELECT * FROM Inventory WHERE ISBN=?"
        data = (str(ISBN),)
        cursor.execute(query, data)
        result = cursor.fetchall()
        

        if (len(result) == 0):
            print("\nThere is no book with this ISBN.")
        ## executes the update once ISBN is verified
        else:
            newStock = int(result[0][7]) - int(quantity)
            query = "UPDATE Inventory SET Stock=? WHERE ISBN=?"
            data = (str(newStock), str(ISBN),)
            cursor.execute(query, data)
            connection.commit()
        cursor.close()

        