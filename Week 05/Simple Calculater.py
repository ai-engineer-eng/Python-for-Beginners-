#defining first function
def sum_cal(a, b):          #two parameters for numbers
    return a+b
#defined second function
def sub_cal(a, b):          #same two parameters fo this function
    return a-b

#defined main function
def calculator():
    operator = input("Enter operator (+, _): ")         #taking operator as input from user
    a = int(input("Enter first name: "))                #asking user to enter first number
    b = int(input("Enter second number: "))             #asking user to enter second number
    
#use of condintional statements to call required function, according to user choosed operator
    if operator == "+":
        # result = sum_cal(a, b)
        # print(f"Resul is: {result}")
        print("Result is ", sum_cal(a, b))

    elif operator == "-":
        print("Result is ", sub_cal(a, b))

#finally called calculator function
calculator()