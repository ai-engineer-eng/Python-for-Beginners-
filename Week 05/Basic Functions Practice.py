                    #avarge calculator

# def cal_avg(num1, num2, num3):        #defined a function; three parameters
#     sum1 = num1+num2+num3         #make sum of three numbers and assign to a variable
#     avg = sum1 / 3                #now average of numbers
#     print(avg)

# cal_avg(7, 94, 58)        #passing arguments; 3 numbers

#......................................................................................................

                    #Length Of List

# def len_ofList(numbers):
#     print(len(numbers))

# nums = [1, 4, 56,7,4,3]
# len_ofList(nums)

#......................................................................................................

                    #Print Items Of List In Single Line

# def elements(line):
    
#     print(line[0], end=" ")       #end= keyword use to end the new line keyword "\n" by defualt in print function
#     print(line[1], end=" ")
#     print(line[2], end=" ")
#     print(line[3], end=" ")
#     print(line[4], end=" ")
#     print(line[5], end=" ")

#we can do this same through for loop
# def list_item(list):
#     for item in list:
#         print(item, end=" ")
# nums = ["HI", "My", "Name", "Is", "Shafqat,", "Beginner", "In Python"]
# list_item(nums)

#......................................................................................................

                                #convert usd to pkr (01 - 08 - 2024)

# def usd_to_pkr(usd):
#     conversion = usd*279
#     print(usd, "USD", "=", conversion, "PKR")


# usd_to_pkr(400)

#......................................................................................................

                                #odd/even string

# def odd_even(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

# odd_even(456453)

#......................................................................................................

                                #Recursion Function

# def recur(n):
#     if n == 0:          #this is "Basic Case" in recursion function, as like "Break" in if statement
#         return
#     print(n)
#     recur(n-1)          #calling function in function itself with argument

# recur(5)

#......................................................................................................

                                #Recursion with factorial

# def fact(n):
#     if (n == 1) or (n == 0):
#         return 1
#     return n*fact(n-1)


# print(fact(5))

#......................................................................................................

                                #recursion function to calculate sum of first natural numbers

# def sum_cal(n):
#     if n == 1:
#         return 1
#     return n+sum_cal(n-1)

# print(sum_cal(10))

#......................................................................................................

                                #recursive function to print all element of list

def list_item(list, index):
    list = [1, 2, 3, 4]
    return list_item()
list_item()