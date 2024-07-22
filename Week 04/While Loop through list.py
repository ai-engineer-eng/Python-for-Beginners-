#You can loop through the list items by using a while loop.
#Use the len() function to determine the length of the list,
# then start at 0 and loop your way through the list items by 
# referring to their indexes.

# books = ["English", "Chemistry", "Physics", "Math"]
# i = 0
# while i < len(books):
#     print(books[i])
#     i+=1

#Looping Using List Comprehension
books = ["English", "Chemistry", "Physics", "Math"]
[print(x) for x in books]