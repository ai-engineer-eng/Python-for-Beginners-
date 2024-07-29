# Once a tuple is created, you cannot change its values. Tuples are unchangeable, 
# or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, 
# and convert the list back into a tuple.

# thistuple = ("Me", "You", "he", "her")
# thislist = list(thistuple)
# # thislist[3] = "they"
# # thistuple = tuple(thislist)

# #we can done this also by using append()
# thislist.append("they")
# thistuple = tuple(thislist)
# print(thistuple)


# 2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want 
# to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
# x = ("a", "b", "c", "d")
# y = ("e", "f")      #created a new tuple of items
# x += y
# print(x)


                #remove items
x = ("a", "b", "c", "d")
y = list(x)
y.remove("c")
x = tuple(y)
print(y)