# class Laptops:
#     # RAM = "8 GB"
#     def __init__(self, name, RAM):
#         print("adding new student in database...")
#         self.name = name
#         self.RAM = RAM

# lap1 = Laptops("HP Elite Book - 3340", "8 GB")
# print(lap1.name, lap1.RAM)
# # print(lap1.RAM)

# class Students():
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def get_avg(self):
#         sum = 0
#         for i in marks:
#             sum += i    
#         print(sum/3)
# marks = [89, 67, 90]
# s1 = Students("Shafqat", marks)
# print(s1.name, s1.marks)
# s1.get_avg()


class Account:
    def __init__(self, Balance, Account_No):
        self.Balance = Balance
        self.Account_No = Account_No

    def debt(self, deb):
        self.Balance -= deb
        print(deb, "PKR","Debted from your account.", "Remaining balance is: ", self.Balance, "PKR")

    def credit(self, cret):
        self.Balance += cret
        print(cret, "PKR", "Credited to your account.", "Total balance is: ", self.Balance, "PKR")




a1 = Account(2000, 903874032)
print(a1.Balance, a1.Account_No)
a1.debt(100)
a1.credit(500)