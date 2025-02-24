# # <=== 1 - masala ===>
# class Oson1:
#     a = 1
#
#     def output_a(self):
#         print(self.a)
#
# Oson1.output_a(Oson1)


# # <== 2 - masala ==>
# class Oson2:
#     a = 3
#     b = 4
#
#     def summa(self):
#         print(self.a + self.b)
#
# Oson2.summa(Oson2)


# # <=== 3 - masala ===>
# class Oson3:
#     a = 10
#
#     def plus_minus(self):
#         if self.a > 0:
#             print("Musbat")
#         elif self.a == 0:
#             print("a 0ga teng")
#         else:
#             print("Manfiy")
#
# Oson3.plus_minus(Oson3)


# # <=== 4 - masala ===>
# class Oson4:
#     a = 5
#
#     def odd_even(self):
#         if self.a % 2 == 0:
#             print("Juft")
#         else:
#             print("Toq")
#
# Oson4.odd_even(Oson4)


# # <=== 5 - masala ===>
# class Oson5:
#     a = 2
#     b = 3
#
#     def daraja(self):
#         print(self.a ** self.b)
#
# Oson5.daraja(Oson5)


# # <=== 6 - masala ===>
# class MyClass6:
#     words = []
#
#     def add_word(self, word):
#         self.words.append(word)
#
#     def remove(self, word):
#         if word in self.words:
#             self.words.remove(word)
#         else:
#             print("Bunday so'z mavjud emas")
#
# MyClass6.add_word(MyClass6, "hello")
# MyClass6.add_word(MyClass6, "world")


# # <=== 7 - masala ===>
# class MyClass7:
#     myDict = {}
#
#     def add_elem(self, key, val):
#         if key not in self.myDict:
#             self.myDict[key] = val
#
#     def update_elem(self, key, val):
#         if key in self.myDict:
#             self.myDict[key] = val
#
#     def print_dict(self):
#         print(self.myDict)
#
# MyClass7.add_elem(MyClass7, "ism1", "shaxriyor")
# MyClass7.add_elem(MyClass7, "ism2", "bekzod")
# MyClass7.add_elem(MyClass7, "ism3", "alisher")
# MyClass7.add_elem(MyClass7, "ism1", "suxrob")
# MyClass7.print_dict(MyClass7)
#
# MyClass7.update_elem(MyClass7, "ism1", "javohir")
# MyClass7.update_elem(MyClass7, "ism4", "ravshan")
# MyClass7.print_dict(MyClass7)


# # # <=== 8 - masala ===>
# class MyClass8:
#     numbers = [1, 2, 7, 5]
#
#     def compare_lists(self, new_list):
#         if sum(self.numbers) > sum(new_list):
#             print("sum(numbers) > sum(new_list)")
#         elif sum(self.numbers) < sum(new_list):
#             print("sum(numbers) < sum(new_list)")
#         else:
#             print("sum(numbers) = sum(new_list)")
#
# MyClass8.compare_lists(MyClass8, [3, 2, 8, 4])
# MyClass8.compare_lists(MyClass8, [1, 4, 2, 1])


# # <=== 9 - masala ===>
# class MyClass9:
#     list1 = [1, 2, 3, 4]
#     list2 = [5, 6, 7, 8]
#
#     def list1_max(self):
#         return max(self.list1)
#
#     def list2_max(self):
#         return max(self.list2)
#
#     def sum_of_two_max(self):
#         max1 = self.list1_max()
#         max2 = self.list2_max()
#         print(max1 + max2)
#
# obj = MyClass9()
# obj.sum_of_two_max()


# # <=== 10 - masala ===>
# class Myclass10:
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     new_numbers = []
#
#     def divide(self, d):
#         for number in self.numbers:
#             if number % d == 0:
#                 self.new_numbers.append(number)
#         return self.new_numbers
#
# obj = Myclass10()
# print(obj.divide(2))