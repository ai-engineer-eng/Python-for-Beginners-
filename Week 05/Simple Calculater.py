def sum_cal(a, b):
    return a+b
def sub_cal(a, b):
    return a-b
def calculator():
    operator = input("Enter operator (+, _): ")
    a = int(input("Enter first name: "))
    b = int(input("Enter second number: "))
    

    if operator == "+":
        # result = sum_cal(a, b)
        # print(f"Resul is: {result}")
        print("Result is ", sum_cal(a, b))

    elif operator == "-":
        print("Result is ", sub_cal(a, b))


calculator()