
# Q.1: Managing an Online Store Inventory Scenario:
# You manage an online store that sells various products. You need to keep track of which
# products are in stock and which are out of stock.

# Use Python sets to manage this inventory.

# Tasks:

# 1. Create a set in_stock containing the products 'laptop', 'mouse', 'keyboard', and 'monitor'.
# 2. Create another set out_of_stock containing 'printer' and 'webcam'.
# 3. A new shipment arrives, restocking the 'printer' and adding a new product 'tablet'.
# Update the in_stock set accordingly.
# 4. A customer reports that the last 'monitor' was sold. Move 'monitor' to the out_of_stock set.
# 5. Find out which products are either in stock or out of stock, but not both.
# 6. Calculate which products are still available for sale.



in_stock = {"laptop","mouse","keyboard","monitor"}
out_stock = {"printer","webcam"}

in_stock.update({"printer","tablet"})
out_stock.remove("printer")

in_stock.remove("monitor")
out_stock.add("monitor")


items = in_stock.symmetric_difference(out_stock)

print("Products Which are and can be available : ",items)
print("product available for sale : ",in_stock)



# Q.2: Student Enrollment System Scenario:
# You are developing a student enrollment system for a university. The university offers
# courses in different subjects, and some students are enrolled in multiple courses.

# Tasks:

# 1. Create a set course_A containing students 'Alice', 'Bob', 'Charlie'.
# 2. Create another set course_B containing students 'Charlie', 'David', 'Eva'.
# 3. Find out which students are enrolled in both course_A and course_B.
# 4. List all students who are enrolled in either course_A or course_B.
# 5. Identify students who are enrolled in course_A but not in course_B.
# 6. Determine the students who are enrolled in only one course.

course_A = {'Alice', 'Bob', 'Charlie'}
course_B = {'Charlie', 'David', 'Eva'}

IN_Both = course_A.intersection(course_B)
Either = course_A.union(course_B)
IN_A = course_A.difference(course_B)
IN_only = Either.difference(IN_Both)

print("students in both courses : ",IN_Both)
print("students in either one course : ",Either)
print("Students only in A course : ",IN_A)
print("students in only one course : " ,IN_only)