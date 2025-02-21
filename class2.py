# # <=== 1 - masala ===> 
# class Texnika:
#     def __init__(self):
#         self.brand = "Apple"
#         self.model = "Macbook"
#         self.type = "Latest GEN"

#     def info(self):
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")
#         print(f"Type: {self.type}\n")

# class NoteBooks(Texnika):
#     def __init__(self):
#         super().__init__()
#         self.video_card = "Apple GPU"
#         self.ram = 8
#         self.displey = "Retina"

#     def more_info(self):
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")
#         print(f"Type: {self.type}")
#         print(f"Video Card: {self.video_card}")
#         print(f"Ram: {self.ram}")
#         print(f"Displey: {self.displey}\n")

# class Televisions(Texnika):
#     def __init__(self):
#         super().__init__()
#         self.model = "TV"
#         self.size = "3840x2160"
#         self.displey = "Oled"

#     def more_info(self):
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")
#         print(f"Type: {self.type}")
#         print(f"Size: {self.size}")
#         print(f"Displey: {self.displey}\n")

# class Smartphones(Texnika):
#     def __init__(self):
#         super().__init__()
#         self.model = "iPhone 16"
#         self.size = "2556x1179"
#         self.sim_count = 2

#     def more_info(self):
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")
#         print(f"Type: {self.type}")
#         print(f"Size: {self.size}")
#         print(f"Sim count: {self.sim_count}\n")

# notebooks = NoteBooks()
# notebooks.more_info()

# televisions = Televisions()
# televisions.more_info()

# smartphones = Smartphones()
# smartphones.more_info()


# # <=== 2 - masala ===>
# class Transport:
#     def __init__(self):
#         self.brand = "Mersedes-Benz"
#         self.model = "AMG"
#         self.type = "sport"
    
#     def info(self):
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")
#         print(f"Type: {self.type}\n")

# class ElentroCars(Transport):
#     def __init__(self):
#         super().__init__()
#         self.battery_life = "500 km"
#         self.charging_time = "5 hour"
    
#     def more_info(self):
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")
#         print(f"Type: {self.type}")
#         print(f"Battery life: {self.battery_life}")
#         print(f"Charging time: {self.charging_time}\n")

# class SportCars(Transport):
#     def __init__(self):
#         super().__init__()
#         self.motor = "6.2 l"
#         self.color = "black"
    
#     def more_info(self):
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")
#         print(f"Type: {self.type}")
#         print(f"Motor: {self.motor}")
#         print(f"Color: {self.color}\n")

# class Truck(Transport):
#     def __init__(self):
#         super().__init__()
#         self.type = "truck"
#         self.motor = "8.1 l"
#         self.height = "2.5 m"
#         self.long = "12 m"
#         self.weight = "5 ton"
    
#     def more_info(self):
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")
#         print(f"Type: {self.type}")
#         print(f"Motor: {self.motor}")
#         print(f"Height: {self.height}")
#         print(f"Long: {self.long}")
#         print(f"Weight: {self.weight}")

# elentroCars = ElentroCars()
# elentroCars.more_info()

# sportcars = SportCars()
# sportcars.more_info()

# truck = Truck()
# truck.more_info()


# <=== 3 - masala ===>
class University:
    def __init__(self):
        self.university = "O'zMU"
    
    def info(self):
        print(f"University: {self.university}")

# # <== 3.1 ==> ------------------------------------>
# class Staff(University):
#     def __init__(self):
#         super().__init__()
#         self.first_name = "Mahmudova"
#         self.last_name = "Nigina"
#         self.age = 34
    
#     def staff_info(self):
#         self.info()
#         print(f"First name: {self.first_name}")
#         print(f"Last name: {self.last_name}")
#         print(f"Age: {self.age}")

# class Student(Staff):
#     def __init__(self):
#         super().__init__()
#         self.group = "24_01"
#         self.first_name = "Ismatov"
#         self.last_name = "Shaxriyor"
#         self.age = 18
    
#     def more_info(self):
#         self.info()
#         print(f"First name: {self.first_name}")
#         print(f"Last name: {self.last_name}")
#         print(f"Group: {self.group}")
#         print(f"Age: {self.age}\n")

# class Teacher(Staff):
#     def __init__(self):
#         super().__init__()
#         self.position = "Lecturer"
#         self.subject = "Tyutor"
    
#     def more_info(self):
#         self.info()
#         print(f"First name: {self.first_name}")
#         print(f"Last name: {self.last_name}")
#         print(f"Position: {self.position}")
#         print(f"Subject: {self.subject}\n")

# class OtherStaff(Staff):
#     def __init__(self):
#         super().__init__()
#         self.first_name = "Po'latov"
#         self.last_name = "Akmal"
#         self.position = "Professor"
    
#     def more_info(self):
#         self.info()
#         print(f"First name: {self.first_name}")
#         print(f"Last name: {self.last_name}")
#         print(f"Position: {self.position}")


# student = Student()
# student.more_info()

# teacher = Teacher()
# teacher.more_info()

# otherstaff = OtherStaff()
# otherstaff.more_info()


# <== 3.2 ==> ------------------------------------>
class Object(University):
    def __init__(self):
        super().__init__()
        self.name = "Mirzo Ulug'bek"
    
    def object_info(self):
        self.info()
        print(f"Name: {self.name}")

class Computers(Object):
    def __init__(self):
        super().__init__()
        self.total_number = 40
        self.os = "Windows 11"
        self.state = "Normal"
    
    def object_more_info(self):
        self.object_info()
        print(f"Total number of computers: {self.total_number}")
        print(f"Operation System: {self.os}")
        print(f"System state: {self.state}\n")

class Mebel(Object):
    def __init__(self):
        super().__init__()
        self.total_number = 120
        self.type = "Soft"
        self.state = "Normal"
    
    def object_more_info(self):
        self.object_info()
        print(f"Total number of mebels: {self.total_number}")
        print(f"Type: {self.type}")
        print(f"Mebel state: {self.state}")


computers = Computers()
computers.object_more_info()

mebel = Mebel()
mebel.object_more_info()
