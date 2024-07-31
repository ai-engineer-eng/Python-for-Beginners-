#In Python a function is defined using the def keyword:

# def fullname(first_name, last_name):         #added two parameters, first_name, last_name
#     print(f"Hi {first_name} {last_name}")    #using formated string to print fullname with message
#     print("How are you?")

# fullname("Shafqat", "Khan")                 #passing arguments to parameters
# fullname("Abid", "Khan")


                            #keyword argument
def number(num, by):
    return num + by


print(number(2, by=3))       #used keyword argument method to make code more readable