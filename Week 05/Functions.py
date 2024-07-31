#In Python a function is defined using the def keyword:

# def fullname(first_name, last_name):         #added two parameters, first_name, last_name
#     print(f"Hi {first_name} {last_name}")    #using formated string to print fullname with message
#     print("How are you?")

# fullname("Shafqat", "Khan")                 #passing arguments to parameters
# fullname("Abid", "Khan")


                            #keyword argument
# def number(num, by):
#     return num + by


# print(number(2, by=3))       #used keyword argument method to make code more readable


                            #optional parameters method
# def fullname(first_name, second_name="Khan"):       #defined a defualt argument to second_name parameter
#     return f"Hi {first_name} {second_name}"


# print(fullname("Shafqat", "Niazi"))                 #if we didn't pass here second argument,
#                                                     #it will use defualt value, but if we pass it will 
                                                    # take value of argument instead of by defualt value


                                #Arbitrary Arguments, *args
#If you do not know how many arguments that will be passed into your function, 
# add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:

def sum(*numbers):
    total = 1
    for number in numbers:              #used for lop to iterate tuple

        total = total + number
    return total

print(sum(2, 3, 4, 6, 7))               #it's output will be in the form of tuple