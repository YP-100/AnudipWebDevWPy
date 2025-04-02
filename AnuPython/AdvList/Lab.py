# 1.You have a list of employee records, and you need to create a new list that contains
# the names of employees who work in the 'Sales' department, all in uppercase
# employees = [
# {"name": "John Doe", "department": "Sales"},
# {"name": "Jane Smith", "department": "Marketing"},
# {"name": "Emily Johnson", "department": "Sales"},
# {"name": "Michael Brown", "department": "HR"}
# ]
employees = [
{"name": "John Doe", "department": "Sales"},
{"name": "Jane Smith", "department": "Marketing"},
{"name": "Emily Johnson", "department": "Sales"},
{"name": "Michael Brown", "department": "HR"}
]

sales_employees = [emp["name"].upper() for emp in employees if emp["department"] == "Sales"]
#converting names in upper and taking only those names whose departmentt section == sales
print(sales_employees)





# 2.You have a list of email addresses and you want to extract the domain part (the part after'@') 
# from each email address.


# emails = [
# "alice@example.com",

# "bob@sample.org",

# "charlie@mydomain.net"
# ]
emails = ["alice@example.com","bob@sample.org","charlie@mydomain.net"]

domains = [email.split('@')[1] for email in emails]
#here taking one cause split will take two diff strings 0 will be of string before@ and 1 will be of after

print(domains)