# # <=== 1 - masala ===>
# pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com"]

# for pochta in pochtalar:
#     if pochta.find("@") != -1:
#         print(f"{pochta} emaili bazada mavjud")
#     else:
#         print(f"Noto'g'ri email: {pochta}")


# # <=== 2 - masala ===>
# passwords = ["password123", "Qwerty!", "admin", "StrongPass1!", "qwertyaa"]

# for passwd in passwords:
#     isSpecChar = False
#     for char in passwd:
#         if char.isalpha():
#             continue
#         else:
#             isSpecChar = True

#     if len(passwd) < 8:
#         print(f"Juda qisqa: {passwd}")
#     elif isSpecChar:
#         print(f"Kuchli parol: {passwd}")
#     else:
#         print(f"Kuchsiz parol: {passwd}")


# # <=== 3 - masala ===>
# haroratlar = [20, 21, 20, 24, 25, 23, 24]

# yigindi = 0
# for i in range(7):
#     yigindi += haroratlar[i]

#     if haroratlar[i] > 22:
#         print(f"{i+1}-kun Iliq kun")
#     else:
#         print(f"{i+1}-kun Salqin kun")

# ort_harorat = yigindi / 7
# print(f"Hafta davomidagi o'rtacha harorat: {ort_harorat}")


# # <=== 4 - masala ===>
# menyu =  ["Osh", "Shashlik", "Manti", "Lag'mon"]
# for taom in menyu:
#     print(taom)

# buyurtma = input("Marhamat, Taom tanlang: ")

# isTrue = False
# for taom in menyu:
#     if taom == buyurtma.capitalize():
#         isTrue = True
#     else:
#         continue

# if isTrue:
#     print("Buyurtmangiz qabul qilindi")
# else:
#     print("Kechirasiz, bunday taom yo'q")


# # <=== 5 - masala ===>
# ages = [16, 21, 17, 30, 25, 15, 19]

# for age in ages:
#     if age < 18:
#         print("Yosh chegarasiga yetmagan")
#     else:
#         print("Xush kelibsiz")


# # <=== 6 - masala ===>
# xabarlar=["Yangi xabar", "Batareya past", "Yangilanish mavjud", "Telegramdan yangi xabar"]

# for xabar in xabarlar:
#     if xabar == "Batareya past":
#         print("Telefoningizni quvvatlang")


# <=== 7 - masala ===>
# fayllar = ["kitob.jpg", "ko_jiguli.mp3", "tabiat.jpg", "malohat.mp3", "Iphohe16.jpg"]

# musiqalar = []
# rasmlar = []

# for fayl in fayllar:
#     if fayl.find(".jpg") != -1:
#         rasmlar.append(fayl)
#     else:
#         musiqalar.append(fayl)

# print(f"musiqalar: {musiqalar}")
# print(f"rasmlar: {rasmlar}")