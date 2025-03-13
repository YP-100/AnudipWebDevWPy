# Objective: Design a simple e-commerce system using Python classes to manage products, customers, and orders.
#  Implement instance variables, class variables, method overloading (simulated), static methods, and class methods. 
# 1. Class Definitions: ● Product Class: ○ Instance Variables:
#  ■ name: The name of the product. 
# ■ price: The price of the product. 
# ■ stock: The quantity available in stock. ○ Class Variables:
#  ■ total_products: A class variable to keep track of the total number of products. 
# ● Customer Class: ○ Instance Variables: 
# ■ name: The name of the customer. 
# ■ email: The email address of the customer. 
# ■ order_history: A list of orders made by the customer. ○ Class Variables:
#  ■ customer_count: A class variable to keep track of the number of customers. 
# ● Order Class: ○ Instance Variables: 
# ■ order_id: The unique ID for the order.
#  ■ customer: The customer who placed the order. 
# ■ products: A dictionary of products and their quantities in the order. ○ Class Variables:
#  ■ order_count: A class variable to keep track of the total number of orders. 

# 2. Initialization: 
# ● Product Class: ○ Initialize with name, price, and stock. Increment the total_products class variable when a new product is added.
#  ● Customer Class: ○ Initialize with name, email, and an empty order_history. Increment the customer_count class variable when a new customer is created. 
# ● Order Class: ○ Initialize with order_id, customer, and an empty dictionary of products. Increment the order_count class variable when a new order is created.

#  3. Instance Methods: 
# ● Product Class: ○ update_stock(quantity): Update the stock quantity when a product is sold or restocked.
#  ● Customer Class: ○ place_order(order): Add an Order instance to the customer's order_history. 
# ● Order Class: ○ add_product(product, quantity): Add a Product and its quantity to the order. 

# 4. Method Overloading (Simulated): 
# ● Product Class: ○ Simulate method overloading with display_info() to show product details in different formats (basic or detailed). 

# 5. Static Methods: 
# ● Product Class: ○ product_info(): A static method to return general information about products. 
# ● Customer Class: ○ customer_info(): A static method to return general information about customers.
#  ● Order Class: ○ order_info(): A static method to return general information about orders.

#  6. Class Methods: 
# ● Product Class: ○ get_total_products(): A class method to return the total number of products. 
# ● Customer Class: ○ get_customer_count(): A class method to return the total number of customers. 
# ● Order Class: ○ get_order_count(): A class method to return the total number of orders. Instructions: 1. Create the Classes: ○ Implement the Product, Customer, and Order classes based on the specifications above.

#  2. Test the Classes: ○ Create instances of Product, Customer, and Order. ○ Add products to the inventory, create orders, and place them for customers. ○ Use the method overloading simulation to display product details in different formats. ○ Call static methods to get general information and class methods to get counts.

class product:
    def __init__(self,name,price,stock):
        total_products = 0
        self.name = name
        self.price = price
        self.stock = stock
        total_products += 1

    def add_stock(self,quantity):
        self.stock += quantity
    def remove_stock(self,quantity):
        self.stock -= quantity

    #method overloading
    def display_info(self,user_type = "reader"):
        if user_type == "admin":                #if admin detailed format  will be showed
            print(f"Product Name: {self.name},Product Price: {self.price},Product Stock: {self.stock}")
        else:
            print(f"Product Name: {self.name},Product Price: {self.price}")

    #static method
    @staticmethod
    def product_info():
        return f"We sell electronics and accessories"
    
    #class method
    @classmethod
    def get_total_products(cls):
        return cls.total_products

class customer:
    def __init__(self,name,email,order_history):
        customer_count = 0
        self.name = name
        self.email = email
        self.order_history = order_history
        customer_count += 1

    def place_order(self,order):
        self.order_history.append(order)

    #static method
    @staticmethod
    def customer_info():
        return f"Welcome to our website"
    
    #class method
    @classmethod
    def get_customer_count(cls):
        return cls.customer_count

class order:
    def __init__(self,order_id,customer,products):
        order_count = 0
        self.order_id = order_id
        self.customer = customer
        self.products = products
        order_count += 1

    def add_product(self,product,quantity):
        self.products[product] = quantity

    #static method
    @staticmethod
    def order_info():
        return f"Order placed successfully"
    
    #class method
    @classmethod
    def get_order_count(cls):
        return cls.order_count
    

# creating instances :
laptop = product("laptop",50000,10)
phone = product("phone",20000,2)
customer1 = customer("yash","yash44@gmail.com",[])
order1 = order(1,customer1,{'laptop':1})

# Adding products to inventory :
laptop.add_stock(5)
phone.add_stock(3)

# creating orders and placing them :
order1.add_product(laptop, 2)  # Customer orders 2 laptops
order1.add_product(phone, 1)   # Customer orders 1 phone
# remove the products from inventory stock
laptop.remove_stock(2)
phone.remove_stock(1)

# Placing the order for the customer :
customer1.place_order(order1)

# displaying product information
laptop.display_info()
laptop.display_info("admin")  # if you are an admin

#calling static methods :
print(product.product_info()) 
print(customer.customer_info()) 
print(order.order_info()) 

#calling class methods:

print(product.get_total_products())
print(customer.get_customer_count())
print(order.get_order_count())
