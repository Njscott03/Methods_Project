class Cart:
## class belongs to Dominic
## should interact with user to link
## userID to the cart transaction
    def __init__(self):
        sample = ""

""" Copy & paste of Design Document

  Class: Cart
  Data 
 -Product IDs: String[]
 -TotalItems: Int
 -TotalPrice: Int
 -ShippingAddress: String
 -ShippingID: String
 -PayementMethod: String
 -Sale: Decimal
 -SaleCode: String




  Functions:
  +addProduct(productID string) :void
  +removeProduct(productID string) :void
  +editProductQuantity(product ID string) :void
  +getShippingAddress() :string
  +setShippingAddress(address String) :string
  +viewCart() :void
  +clearCart() :void
  +getPaymentMethod() :string
  +setPaymentMethod(payment String) :void
  +getSale() : Decimal
  +setSale(Sale Decimal) :void

  +addSalesCode(code String)
  +Order()






 
  +addProduct(productID string) - adds product to list of products in the cart
  +removeProduct(productID string) - removes product from a list of products in the cart
  +editProductQuantity(product ID string) -changes product quantity of one item
  +getShippingAddress() -returns shipping address 
  +setShippingAddress(address String) - changes shipping address
  +viewCart() -displays cart information
  +clearCart() -removes all cart information
  +getPaymentMethod() - returns current payment method
  +setPaymentMethod(payment String) - changes payment method
  +addSalesCode(code String) -if valid code change total price of the cart.
  +Order() - moves on to the order class and sends out info to corresponding services
  +getSale() - return sale percentage 
  +setSale(Sale Decimal) -changes sale percentage


"""
"""      TO DO------------------
        -set up a phoney menu for the cart // do before check in 2
        -figure out how to interact with the database using python code.
        -define the get functions
        -define the set functions
        
        
"""
