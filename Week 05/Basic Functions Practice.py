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

def usd_to_pkr(usd):
    conversion = usd*279
    print(usd, "USD", "=", conversion, "PKR")


usd_to_pkr(400)