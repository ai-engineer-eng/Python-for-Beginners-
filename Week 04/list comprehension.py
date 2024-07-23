#List comprehension offers a shorter syntax when you want to create a new list based on
# the values of an existing list.
#Based on a list of fruits, you want a new list, containing only the fruits with the letter
# "a" in the name.
#Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ["apple", "banana", "cherry", "mango", "kiwi"]
newlist = []
# for x in fruits:
#     if "a" in x:
#         newlist.append(x)
# print(newlist)

#now with list comprehension method #shorter syntax

# newlist = [x for x in fruits if "a" in x]
# print(newlist)

#Condition
#The condition is like a filter that only accepts the items that valuate to True.

newlist = [x for x in fruits if x!="cherry"]
print(newlist)