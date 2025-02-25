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


# """ ------------ Class Method Tasks ------------ """
# # <=== 6 - masala ===>
# class Dog:
#     total_dogs = 0
    
#     def __init__(self):
#         Dog.total_dogs += 1

#     @classmethod
#     def get_total_dogs(cls):
#         return cls.total_dogs

# dog = Dog()
# dog = Dog()
# dog = Dog()
# dog = Dog()
# print(dog.get_total_dogs())


# # <=== 7 - masala ===>
# class Computer:
#     total_computers = 0
#     computers_list = []

#     def __init__(self, comp):
#         Computer.total_computers += 1
#         Computer.computers_list.append(comp)
    
#     @classmethod
#     def add_computer(cls):
#         return cls.total_computers, cls.computers_list

# comp = Computer("Macbook Pro")
# comp = Computer("Asus TUF Gaming")
# comp = Computer("HP Victus")
# comp = Computer("Lenovo Legion")
# total_computers, computers_list = comp.add_computer()
# print(total_computers)
# print(computers_list)


# # <=== 8 - masala ===>
# class Employee:
#     total_employees = 0
#     employees_list = []

#     def __init__(self, employee):
#         Employee.total_employees += 1
#         Employee.employees_list.append(employee)
    
#     @classmethod
#     def hire_employee(cls):
#         return cls.total_employees, cls.employees_list

# employee = Employee("John")
# employee = Employee("Anna")
# employee = Employee("Dazy")
# total_employes, employees_list = Employee.hire_employee()
# print(total_employes) 
# print(employees_list) 


# # <=== 9 - masala ===>
# class Television:
#     average_screen_size = 0
#     count = 0

#     def __init__(self, screen_size):
#         Television.count += 1
#         Television.average_screen_size = (Television.average_screen_size * (Television.count - 1) + screen_size) / Television.count
    
#     @classmethod
#     def update_average_screen_size(cls):
#         return cls.average_screen_size
#     @classmethod
#     def total_tvs(cls):
#         return cls.count

# television = Television(32)
# television = Television(43)
# television = Television(54)
# print(Television.update_average_screen_size())
# print(Television.total_tvs())


# # <=== 10 - masala ===>
# class Course:
#     total_courses = 0
#     courses_list = []

#     def __init__(self, course):
#         self.add_course(course)
    
#     @classmethod
#     def add_course(cls, course):
#         cls.total_courses += 1
#         cls.courses_list.append(course)

# course = Course("python")
# course = Course("javascript")
# course = Course("java")
# course = Course("flutter")
# course = Course("nodejs")
# print(Course.total_courses)
# print(Course.courses_list)


""" ------------ Static Method Tasks ------------ """
# # <=== 11 - masala ===>
# class Math:
#     @staticmethod
#     def multiply(a, b):
#         return a * b

# print(Math.multiply(2, 5))
# print(Math.multiply(3, 6))
# print(Math.multiply(8, 4))


# # <=== 12 - masala ===>
# class Temperature:
#     @staticmethod
#     def celsius_to_fahrenheit(temp):
#         return (temp * (9 / 5)) + 32

# print(Temperature.celsius_to_fahrenheit(20))
# print(Temperature.celsius_to_fahrenheit(25))
# print(Temperature.celsius_to_fahrenheit(32))


# # <=== 13 - masala ===>
# class Distance:
#     @staticmethod
#     def miles_to_kilometers(mile):
#         return mile * 1.60934

# print(Distance.miles_to_kilometers(10))
# print(Distance.miles_to_kilometers(450))
# print(Distance.miles_to_kilometers(60))


# # <=== 14 - masala ===>
# class Utility:
#     @staticmethod
#     def is_even(char):
#         if isinstance(char, int) or isinstance(char, float) or isinstance(char, complex) or char.isdigit():
#             return True
#         else:
#             return False

# print(Utility.is_even(12))
# print(Utility.is_even("hello"))
# print(Utility.is_even("10"))
# print(Utility.is_even(2j))
# print(Utility.is_even(2.3))


# # <=== 15 - masala ===>
# class Time:
#     @staticmethod
#     def seconds_to_minutes(s):
#         return (s // 60, s % 60) # (minut, second)

# print(Time.seconds_to_minutes(72))
# print(Time.seconds_to_minutes(114))
# print(Time.seconds_to_minutes(231)) 