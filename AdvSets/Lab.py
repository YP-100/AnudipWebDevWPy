# Restaurant Management System :  
# Scenario: You are helping a restaurant manage its menu. The restaurant has a regular menu and a special weekend menu. 
# Tasks: 
# 1. Create a set regular_menu with items 'pizza', 'burger', 'salad', and 'pasta'. 
# 2. Create another set weekend_menu with items 'steak', 'salmon', 'pasta', and 'wine'. 
# 3. Find out which items are available on both the regular and weekend menus.
# 4. Determine the items that are only available on the weekend. 
# 5. Add a new item 'dessert' to both menus.
# 6. The restaurant decides to stop offering 'burger'. Remove it from the regular menu.

regural_menu = {'pizza', 'burger', 'salad', 'pasta'}
weekend_menu = {'steak', 'salmon', 'pasta', 'wine'}
Available_Both = regural_menu.intersection(weekend_menu)
print("Available on both regular and weekends : ",Available_Both)
regural_menu.add("dessert")
weekend_menu.add("dessert")
regural_menu.remove("burger")

print("New regular menu : ",regural_menu)
print("New weekend menu : ",weekend_menu)



#  Event Management System 
# Scenario: You are organizing a large event and need to manage the list of attendees. Some attendees have VIP access, while others do not. 
# Tasks: 1. Create a set of attendees with names 'John', 'Jane', 'Emily', and 'Michael'. 
# 2. Create a frozenset vip_attendees with names 'Jane' and 'Michael'. 
# 3. A new attendee 'Sarah' registers for the event. Add her to the attendees set. 
# 4. Check if 'Emily' is a VIP attendee.
# 5. Find out which attendees have either regular or VIP access but not both. 
# 6. List all attendees with either regular or VIP access.

attendees = {'John', 'Jane', 'Emily', 'Michael'}
vip_attendees = {'Jane','Michael'}
attendees.add("sarah")
print(vip_attendees.__contains__("Emily"))
IN_Both = attendees.intersection(vip_attendees)
both = attendees.union(vip_attendees)
Either = both.difference(IN_Both)

print("Attendees in either Attendees or vip and not both : ",Either)
print("Attendees with either vip or regular access : ",both)