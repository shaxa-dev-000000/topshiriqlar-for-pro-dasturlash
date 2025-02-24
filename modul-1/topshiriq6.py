# # <=== 1 - masala ===>
# def user_data(first_name, last_name, age):
#     print(f"Ism: {first_name}")
#     print(f"Familya: {last_name}")
#     print(f"Yosh: {age}")

# first_name = input("Ismingizni kiriting: ")
# last_name = input("Familyangizni kiriting: ")
# age = input("Yoshingizni kiriting: ")

# user_data(first_name, last_name, age)


# # <=== 2 - masala ===>
# def find_max(a, b, c):
#     if a == b == c:
#         print(f"Eng katta son - A va B va C = {a}")
#     elif a == b > c:
#         print(f"Eng katta son - A va B = {a}")
#     elif a == c > b:
#         print(f"Eng katta son - A va C = {a}")
#     elif b == c > a:
#         print(f"Eng katta son - B va C = {b}")
#     elif a > b > c or a > c > b:
#         print(f"Eng katta son - A = {a}")
#     elif b > a > c or b > c > a:
#         print(f"Eng katta son - B = {b}")
#     else:
#         print(f"Eng katta son - C = {c}")

# a = int(input("A = "))
# b = int(input("B = "))
# c = int(input("C = "))
# find_max(a, b, c)


# # <=== 3 - masala ===>
# def find_letter_count(word, letter):
#     i = 0
#     for char in word:
#         if char == letter:
#             i +=1
#     print(f"{letter} harfi {word} so'zida {i} marta qatnashgan")

# word = input("So'z kiriting: ")
# letter = input("Qaysi harfni tekshirmoqchisiz: ")

# find_letter_count(word, letter)


# # <=== 4 - masala ===>
# def list_sum(myList):
#     sum = 0
#     for digit in myList:
#         sum += digit
#     print(f"Listning elementlar yig'indisi {sum}")

# myList = [2, 6, 12, 21, 10, 14, 5]
# list_sum(myList)


# # <=== 5 - masala ===>
# def daraja(a, b):
#     print(f"{a} ning {b}-darajasi: {a**b}")

# a = int(input("Son kiriting: "))
# b = int(input("Sonning darajasini kiriting: "))
# daraja(a, b)


# # <=== 6 - masala ===>
# def daraja4(a, b, c, d):
#     print(f"{a} ning {b}-darajasi: {a**b}")
#     print(f"{c} ning {d}-darajasi: {c**d}")

# a = int(input("1-sonni kiriting: "))
# b = int(input("1-sonning darajasini kiriting: "))
# c = int(input("2-sonni kiriting: "))
# d = int(input("2-sonning darajasini kiriting: "))

# daraja4(a, b, c, d)


# # <=== 7 - masala ===>
# def digit_count_and_sum(word):
#     sum = 0
#     digit_count = 0
#     for char in word:
#         if char.isdigit():
#             digit_count += 1
#             sum += int(char)
#     print(f"{word} so'zida {digit_count} ta raqam bor va bu raqamlar yig'indisi {sum}")

# word = input("So'z kiriting: ")

# digit_count_and_sum(word)


# # <=== 8 - masala ===>
# def add_right(a, b):
#     print(f"Natija: {b}{a}")

# a = input("A sonni kiriting: ")
# b = input("B sonni kiriting: ")

# add_right(a, b)


# # <=== 9 - masala ===>
# def add_left(a, b):
#     print(f"Natija: {a}{b}")

# a = input("A sonni kiriting: ")
# b = input("B sonni kiriting: ")

# add_left(a, b)


# # <=== 10 - masala ===>
# def work_with_list(a):
#     digit1 = a[0]
#     i = 0
#     while i < len(a) - 1:
#         digit2 = a[i + 1]
#         if digit1 < digit2:
#             pass
#         else:
#             digit1 = digit2
#         i += 1
    
#     print(f"Eng kichik son: {digit1}")
    
#     new_a = []
#     for i in a:
#         if i == digit1:
#             continue
#         else:
#             new_a.append(i * digit1)
    
#     print(f"New list: {new_a}")

# a = [3, 7, 12, 9, 20, 2, 16, 7, 14]
# print(f"Old list: {a}")

# work_with_list(a)


# # <=== 11 - masala ===>
# def big_sales(sales):
#     keys = list(sales.keys())
#     sums = list(sales.values())

#     max_sum = max(sums)
#     max_sum_index = sums.index(max_sum)
    
#     print(f"Eng ko'p {keys[max_sum_index]} oyida {max_sum} ta mahsulot sotilgan")



# sales = {
#     "yanvar": 12000,
#     "mart": 6000,
#     "aprel": 15000,
#     "sentabr": 9000,
#     "dekabr": 10000,
# }

# big_sales(sales)


# # <=== 12 - masala ===>
# def min_max(numbers, max_num, min_num):
#     max_digit = max(numbers)
#     min_digit = min(numbers)

#     if max_digit == max_num:
#         print(f"To'g'ri, {max_num} eng katta son")
#     else:
#         print(f"Noto'g'ri {max_num} eng katta son emas")
    
#     if min_digit == min_num:
#         print(f"To'g'ri, {min_num} eng kichik son")
#     else:
#         print(f"Noto'g'ri {min_num} eng kichik son emas")

# numbers = [3, 7, 12, 9, 20, 2, 16, 7, 14]
# max_num = 16
# min_num = 2

# min_max(numbers, max_num, min_num)


# # <=== 13 - masala ===>
# def expensiveProduct(products):
#     prices = []
#     phone_names = []

#     for i in products:
#         prices.append(i['price'])
#         phone_names.append(i['name'])
    
#     max_price = max(prices)
#     max_price_index = prices.index(max_price)
#     phone_name = phone_names[max_price_index]

#     print(f"Eng qimmat telefon bu {phone_name}, uning narxi {max_price}$")


# products = [
#     {
#         "name": "Iphone X",
#         "price": 600
#     },
#     {
#         "name": "Iphone 12",
#         "price": 1500
#     },
#     {
#         "name": "Samsung Note 9",
#         "price": 800
#     },
#     {
#         "name": "Samsung S10",
#         "price": 1100
#     },
# ]

# expensiveProduct(products)