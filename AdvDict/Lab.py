# 1. You have a list of user data with their names and email addresses. Create a
# dictionary that maps each domain (from the email address) to a list of users with
# emails from that domain.


users = [
    {"name": "Yash", "email": "yash@example.com"},
    {"name": "Ram", "email": "ram@gmail.com"},
    {"name": "Sakshi", "email": "sakshi@example.com"},
    {"name": "virat", "email": "virat@yahoo.com"},
    {"name": "Divya", "email": "divya@gmail.com"}
]

domains = {user["email"].split("@")[1] for user in users}
# will split user.email and get the part on index 1 and save it in a new dictionary
domain_users = {domain: [user["name"] for user in users if user["email"].split("@")[1] == domain] for domain in domains}
#will compair domains in man dictionary with domain in domains dictionary 

print(domain_users)


# 2. You have a list of customer reviews for different products. Each review
# contains a product name and a rating. Your task is to create a dictionary that
# maps each product to its average rating.

# Sample customer reviews
reviews = [
    {"product": "Laptop", "rating": 3.0},
    {"product": "Phone", "rating": 5.0},
    {"product": "Laptop", "rating": 4.5},
    {"product": "Tablet", "rating": 2.0},
    {"product": "Phone", "rating": 3.8},
    {"product": "Tablet", "rating": 4.2}
]

products = {review["product"] for review in reviews}

product_ratings = {
    product: sum(review["rating"] for review in reviews if review["product"] == product) / 
             sum(1 for review in reviews if review["product"] == product)
             #will divide sum of all reviews by no of product like 8.5/2 for laptop 
    for product in products
}

print(product_ratings)
