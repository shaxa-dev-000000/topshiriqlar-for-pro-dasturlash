""" ------------ Instance Method Tasks ------------ """
# # <=== 1 - masala ===>
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
    
#     def deposit(self, deposit_money):
#         self.balance += deposit_money
#         print("Your money has been deposited")
    
#     def withdraw(self, withdraw_money):
#         if withdraw_money > self.balance:
#             print("You don't have enough money in your account")
#         else:
#             self.balance -= withdraw_money
#             print("your money has been withdrawn")

#     def check_balance(self):
#         print(f"Your balance: {self.balance}")

# myBalance = BankAccount(1000)
# myBalance.deposit(500) # balance: 1000 + 500 = 1500
# myBalance.withdraw(2000) # 2000 > 1500: You don't have enough money in your account
# myBalance.withdraw(700) # balance: 1500 - 700 = 800
# myBalance.check_balance()


# <=== 2 - masala ===>
class Rectangle:
    def __init__(self, length, width):
        self.lenght = length
        self.width = width
    
    def area(self):
        area = self.lenght * self.width
        print(f"Surface area of a rectangle: {area}")
    
    def perimetr(self):
        perimetr = 2 * (self.lenght + self.width)
        print(f"The perimeter of the rectangle: {perimetr}")
    
    def is_square(self):
        print(f"Is it a square: {self.lenght == self.width}")

rectangle1 = Rectangle(10, 15)
rectangle1.area()
rectangle1.perimetr()
rectangle1.is_square()

print("")

rectangle2 = Rectangle(12, 12)
rectangle1.area()
rectangle1.perimetr()
rectangle1.is_square()
