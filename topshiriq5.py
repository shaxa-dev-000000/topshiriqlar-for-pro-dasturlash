# <------------------- Tasks in "while tasks.txt" -------------------->

# # <=== 1 - masala ===>
# i = 0
# while i < 5:
#     print(f"{i+1}"*(i+1))
#     i += 1


# # <=== 2 - masala ===>
# number = input("Son kiriting: ")

# i = 0
# result = 0
# while i < len(number):
#     result += int(number[i])
#     i += 1

# print("Natija:", result)


# # <=== 3 - masala ===>
# result = 0

# i = 1
# while i < 101:
#     if i % 2 != 0:
#         result += i
#     i += 1

# print("Natija:", result)


# # <=== 4 - masala ===>
# import random

# rdm_number = random.randint(1, 100)
# input_number = int(input("Kompyuter o'ylangan sonni toping. Taxminiy son kiriting: "))

# while True:
#     if rdm_number < input_number:
#         print("Juda baland!")
#     elif rdm_number > input_number:
#         print("Juda past!")
#     else:
#         print(f"Tabriklayman to'g'ri topdingiz. Kompyuter o'ylagan son {rdm_number} edi")
#         break
#     input_number = int(input("Yana bir bor urinib ko'ring: "))


# <------------------- Tasks in "while sikli.pdf" -------------------->

# # <=== 1 - masala ===>
# color = input("Sfetafor qaysi rangni ko'rsatmoqda: ")

# while True:
#     if color == 'qizil' or color == 'yashil' or color == 'sariq':
#         print("rahmat, to'g'ri keladi")
#         break
#     else:
#         color = input("Iltimos to'g'ri rangni kiriting: ")


# # <=== 2 - masala ===>
# import random as rdm

# rdm_number = rdm.randint(1, 10)
# input_number = int(input("Kompyuter o'ylagan sonni kiriting: "))

# while True:
#     if rdm_number == input_number:
#         print("Tabriklaymiz, siz topdingiz!")
#         break
#     else:
#         input_number = int(input("Noto'g'ri, qayta urinib ko'ring: "))


# # <=== 3 - masala ===>
# friends_list = []

# while True:
#     friend = input("Do'stingizni ismini kiriting(Agar so'rovni to'xtatmoqchi bo'lsangiz 'stop' so'zini yozing): ")
#     if friend == 'stop':
#         break
#     friends_list.append(friend)

# print("Do'stlaringiz ro'yxati: ", friends_list)


# # <=== 4 - masala ===>
# valyuta = input("Qaysi valyutani ayrboshlamoqchisiz(1 USD = 12.600 UZS): \n1. USD -> UZS \n2. UZS -> USD \n-> ")

# if valyuta == "1":
#     while True:
#         sum = input("Qancha pulni ayrboshlamoqchisiz(chiqish uchun 'exit' so'zini yozing): ")
#         if sum == "exit":
#             break
#         else:
#             print(f"{sum} dollar {int(sum)*12600} so'mga teng bo'ladi")
# elif valyuta == "2":
#     while True:
#         sum = input("Qancha pulni ayrboshlamoqchisiz(chiqish uchun 'exit' so'zini yozing): ")
#         if sum == "exit":
#             break
#         else:
#             print(f"{sum} so'm {int(sum)/12600} dollarga teng bo'ladi")