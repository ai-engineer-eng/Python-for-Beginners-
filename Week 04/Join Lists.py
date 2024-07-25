# There are several ways to join, or concatenate, two or more lists in Python.

# One of the easiest ways are by using the + operator.
list1 = ["Ronaldo", "Messi", "Mbape"]
list2 = [1, 2, 3]
# list3 = list1 + list2

#another way
# for x in list1:
#     list2.append(x)
# print(list2)

#or we can use extend() method
list1.extend(list2)
print(list1)