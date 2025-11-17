# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
###################################################################################################
# collections are covered to store multiple items in a single variable
# lists are ordered collections of items
# lists are mutable, meaning you can change their content
# lists are created using square brackets []

list_of_fruits = ["apple", "banana", "cherry", "date"]
print (list_of_fruits) # ['apple', 'banana', 'cherry', 'date']
print(type(list_of_fruits)) 
#Acessing items in a list
print(list_of_fruits[0])
print(list_of_fruits[1]) 
print (list_of_fruits[-1])
print(list_of_fruits[1:3]) 
#reverse the list
list_of_fruits.reverse() 
print(list_of_fruits[::-1]) 
#appending items to a list
list_of_fruits.append("elderberry")
print(list_of_fruits)
list_of_fruits.append("strawberry")
print(list_of_fruits)
list_of_fruits.append("plum")
print(list_of_fruits)
#to add multiple items in a list
list_of_fruits.extend(["honeyfruit", "dragonfruit", "grape"])
print(list_of_fruits)
#revrse a list
list_of_fruits.reverse()
print(list_of_fruits)

#popping item from a list
popped_item = list_of_fruits.pop()
print(popped_item)
print(list_of_fruits)
#inserting item at specific index
list_of_fruits.insert(1,"blueberry")
print(list_of_fruits) 
#removing a specific item
list_of_fruits.remove("banana") 
print(list_of_fruits) #['grape', 'blueberry', 'dragonfruit', 'honeyfruit', 'plum', 'strawberry', 'elderberry', 'apple', 'cherry']
list_of_fruits.insert(3,"banana")
list_of_fruits.sort()
print(list_of_fruits)

list_of_items = list(range(1,101))
print(list_of_items) 
list_of_items = list(range(1,1001))
print(list_of_items) 
print(len(list_of_items))


#why use list
#instead of creating variables
#for each item, we can store them in a list
#this makes our job easier
#this makes managing the complexity of our code easier 
#when we need to manage multiple items
#performance task answser!!!!!!!!!!!!!!!!!!


#SETS AND TUPLESZ 
set1= {1, 2, 3, 4, 5} 
set2= {"apple", "banana", "cherry"} 
print(set1)
print(set2)
print(type(set1))

set_with_duplicates = {1, 2, 3, 4, 5} 
print(set_with_duplicates) 

print(3 in set1) #tru 
print (6 in set1) #false

#tuple examples
tuple1= (1, 2, 3, 4, 5) 
tuple2= ("apple", "banana", "cherry")
print(tuple1) 
print(tuple2) 
print(type(tuple1))
#why are tuples used instead of lists
#tuples are immunable (cannot change them)
#useful for data that should not be modified

social_security_number = (123444, 4444445, 5676789)
# Examples:

# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.

# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.