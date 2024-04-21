from user import *
import sqlite3
import sys

## class belongs to Dominic
## should interact with user 
## to link userID to the cart transaction
class Cart:

    ##constructor
    def __init__(self):        ## does the database have to be the same as the user database?
        self.database = user.database
        databaseName: string
        
    def cartMenu(user): ## receving user class to track userID to cart
        while(1)
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
            if(option == "1"):
                cart.viewCart(user.userID())   ## test if the () after userID is needed
                
            ## Add To Cart
            if(option == "2"):
                cart.viewCart(user.userID(), ISBN, quantity)
                
            ## Remove From Cart
            if(option == "3"):
                cart.viewCart(user.userID(), ISBN)
    
            ## Check Out
            if(option == "4"):
                cart.viewCart(user.userID())


        
        print("Successfully Left Cart Information.")
        print()

    def viewCart(string userID): 
        ## display database linked to cart
        
    def addToCart(string userID, string ISBN, int quantity): 
        ## add to database linked to cart
    
    def removeFromCart(string userID, string ISBN): 
        ## remove from database linked to cart
        
    def checkOut(string userID): 
        ## calls inventory to decrease stock
        ## calls orderHistory to make an order and fill out that order
        

"""      TO DO------------------
        -fix cart initialization
        -figure out how to interact with the database using python code.
        -Prioritize completing Add and view cart
        -Prioritize completing remove from cart
        -finish checkout -----------------takes the longest so dont procrastinate
        
        
        
        
"""
