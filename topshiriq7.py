# # <=== 1 - masala ===>
# def str_counter(strs):
#     result = []
#     for i in strs:
#         result.append([len(i), i])
#     return dict(result)

# strs = ["shaftoli", "olma", "nok" ]
# print(str_counter(strs))


# # <=== 2 - masala ===>
# def merge_list(list_1 ,list_2):
#     if len(list_1) == len(list_2):
#         result = []
#         for i in range(len(list_1)):
#             result.append([list_1[i], list_2[i]])
#         return dict(result)
#     else:
#         return "list_1 != list_2"

# alpha = ['a', 'b', 'c']
# num = [1, 2, 3]

# print(merge_list(alpha, num))


# # <=== 3 - masala ===>
# contacts = {
#     "Nodir": "+998918602711",
#     "Laziz": "+998908002534"
# }

# while True:
#     print("Kontaktlar ro'yxati: ", contacts)
#     bolim = input("Bo'limni tanlang: \n1. Kontakt qo'shish \n2. Yangilash \n3. Kontaktni o'chirish \n4. Qidirish \n5. Chiqish \n-> ")

#     if bolim == "1":
#         contactName = input("Kontakt nomini kiriting: ")
#         contactNumber = input("Kontakt nomini kiriting: ")

#         newContact = [contactName, contactNumber]
#         contacts[contactName] = contactNumber
#     elif bolim == "2":
#         updateContact = input("Qaysi kontaktni yangilamoqchisiz: ")
#         if updateContact.capitalize() in contacts:
#             updateContactNumber = input("Yangi raqamni kiriting: ")
#             contacts[updateContact.capitalize()] = updateContactNumber
#         else:
#             print("Bu kontakt mavjud emas")
#     elif bolim == "3":
#         deleteContact = input("Qaysi kontaktni o'chirmoqchisiz: ")
#         if deleteContact.capitalize() in contacts:
#             del contacts[deleteContact.capitalize()]
#         else:
#             print("Bu kontakt mavjud emas")
#     elif bolim == "4":
#         findContact = input("Qaysi kontakt haqida bilmoqchisiz: ")
#         if findContact.capitalize() in contacts:
#             aboutContact = contacts[findContact.capitalize()]
#             print(f"Bu kontaktning raqami {aboutContact}")
#     elif bolim == "5":
#         break
#     else:
#         print("Xato bo'lim")


# # <=== 4 - masala ===>
# from collections import Counter

# def counter_dict(nums):
#     x = Counter(nums)
#     return x

# numbers = [1, 1, 2, 3, 2, 1, 4, 2]
# count_nums = dict(counter_dict(numbers))

# print(f"counter_dict({numbers}) -> {count_nums}")


# # <=== 5 - masala ===>
# def max_ball_students(talabalar):
#     students = []
#     for i in talabalar.items():
#         students.append(i)
    
#     max_bal1 = students[0][1]
#     for i in range(len(students) - 1):
#         max_bal2 = students[i + 1][1]
#         if max_bal2 < max_bal1:
#             pass
#         else:
#             a = max_bal1
#             max_bal1 = max_bal2
#             max_bal2 = a
    
#     f_s_students = []
#     for i in students:
#         if max_bal1 in i or max_bal2 in i:
#             f_s_students.append(i)
    
#     return dict(f_s_students)

# talabalar = {"Akmal":64, "Tohir":55, "Nodir":76, "Zafar":80}

# print(f"{talabalar} -> {max_ball_students(talabalar)}")
