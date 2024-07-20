#Create a simple program to manage a grocery list.

#created a empty list to take items from user.
grocery_list = []

#Step 2: ask the user how many items want to add in list
numbers = int(input("How many items you want to add? "))

# Step 3: Use a for loop to allow the user to input the items one by one
for number in range(numbers):
    item = input(f"Enter item {number+1}: ").lower()
    grocery_list.append(item)

# Step 4: Print the complete grocery list
print("Here is your Grocery List: " + str(grocery_list))

# Step 5: Ask the user if they want to remove any items from the list
askuser = input("Do you want to remove any item from the list? ").lower()
if askuser == "yes":
    print("Ok, let's do it!")
else:
    quit()
item_remove = input("Which item you want to remove? ").lower()
if item_remove in grocery_list:
    grocery_list.remove(item_remove)
    print("Updated Grocery List: " + str(grocery_list))
else:
    print(f"{item_remove} is not in the list.")