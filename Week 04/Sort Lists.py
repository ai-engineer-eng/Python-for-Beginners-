#List objects have a sort() method that will sort the list alphanumerically, ascending, 
# by default:

# players = ["Ronaldo", "Messi", "Mbape", "David"]
# players.sort()
# print(players)

#sort the list numerically

#numbers = [100, 40, 38, 98, 23, 5]
# numbers.sort()
# print(numbers)

#To sort descending, use the keyword argument reverse = True:

# numbers.sort(reverse=True)
# print(numbers)

#You can also customize your own function by using the keyword argument key = function.

#The function will return a number that will be used to sort the list (the lowest number first):

# def myfunc(n):
#     return abs(n - 2)
# numbers.sort(key=myfunc)
# print(numbers)

#By default the sort() method is case sensitive, resulting in all capital letters being
# sorted before lower case letters:
fruits = ["apple", "Banana", "Mango", "Duck"]
# fruits.sort()
# print(fruits)

#So if you want a case-insensitive sort function, use str.lower as a key function:
# fruits.sort(key=str.lower)
# print(fruits)
fruits.reverse()
print(fruits)