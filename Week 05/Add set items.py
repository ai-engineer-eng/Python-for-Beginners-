# Once a set is created, you cannot change its items, but you can add new items.
# To add one item to a set use the add() method.

# language = {"Python", "c++", "c"}
# language.add("Java")
# print(language)


# Add Sets
# To add items from another set into the current set, use the update() method.

language = {"python", "c++", "c"}
# program = {"test", "react"}
# language.update(program)
# print(language)


# Add Any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object 
# (tuples, lists, dictionaries etc.).
program = ["react", "php"]
language.update(program)
print(language)