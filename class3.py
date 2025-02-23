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


# # <=== 2 - masala ===>
# class Rectangle:
#     def __init__(self, length, width):
#         self.lenght = length
#         self.width = width
    
#     def area(self):
#         area = self.lenght * self.width
#         print(f"Surface area of a rectangle: {area}")
    
#     def perimetr(self):
#         perimetr = 2 * (self.lenght + self.width)
#         print(f"The perimeter of the rectangle: {perimetr}")
    
#     def is_square(self):
#         print(f"Is it a square: {self.lenght == self.width}")

# rectangle1 = Rectangle(10, 15)
# rectangle1.area()
# rectangle1.perimetr()
# rectangle1.is_square()

# print("")

# rectangle2 = Rectangle(12, 12)
# rectangle1.area()
# rectangle1.perimetr()
# rectangle1.is_square()


# # <=== 3 - masala ===>
# class Student:
#     def __init__(self, name, age, grades):
#         self.name = name
#         self.age = age
#         self.grades = grades
    
#     def add_grade(self, grade):
#         self.grades.append(grade)
#         print("Grade added.")
    
#     def calculate_average(self):
#         sum = 0
#         for grade in self.grades:
#             sum += grade
#         self.sum_gardes = sum / len(self.grades)
#         print(f"{self.name}'s average grade: {self.sum_gardes:.2f}")
    
#     def print_summary(self):
#         if self.sum_gardes >= 4:
#             print(f"{self.name}'s mastering is excellent {self}")
#         elif 2 < self.sum_gardes < 4:
#             print(f"{self.name}'s good to master")
#         else:
#             print(f"{self.name}'s poor mastery")

# student = Student("shaxriyor", 18, [4, 4, 3, 5, 4])
# student.add_grade(3)
# student.calculate_average()
# student.print_summary()


# # <=== 4 - masala ===>
# from math import pi

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
    
#     def circle_area(self):
#         area = pi * (self.radius**2)
#         print(f"The surface of the circle: {area:.2f}")
    
#     def circle_circumference(self):
#         circumference = 2 * pi * self.radius
#         print(f"the circumference of a circle: {circumference:.2f}")
    
#     def circle_diametr(self):
#         diametr = 2 * self.radius
#         print(f"the diametr of a circle: {diametr}")

# circle = Circle(10)
# circle.circle_area()
# circle.circle_circumference()
# circle.circle_diametr()


# # <=== 5 - masala ===>
# class Book:
#     def __init__(self, title, author, current_page):
#         self.title = title
#         self.author = author
#         self.current_page = current_page
    
#     def open(self, page):
#         self.current_page = page
#         print(f"Book page: {self.current_page}")

#     def turn_page(self):
#         self.current_page += 1
#         print("Moved to the next page")
#         print(f"Book page: {self.current_page}")
    
#     def restart(self):
#         self.current_page = 1
#         print("Moved to page 1")
#         print(f"Book page: {self.current_page}")

# book = Book("Crime and Punishment", "Fyodor Dostoevsky", 20)
# book.open(45)
# book.turn_page()
# book.turn_page()
# book.turn_page()
# book.turn_page()
# book.restart()
# book.turn_page()


