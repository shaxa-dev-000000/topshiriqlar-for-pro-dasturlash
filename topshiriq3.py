# # <=== 1 - masala ===>
# harorat = float(input("Ob-havo haroratini kiriting: "))

# if harorat < 0:
#     print("Sovuq")
# elif 0 <= harorat <= 20:
#     print("Salqin")
# elif 21 <= harorat <= 30:
#     print("Iliq")
# else:
#     print("Issiq")


# # <=== 2 - masala ===>
# xarid_summasi = int(input("Xarid summasini kiriting: "))

# if xarid_summasi < 50000:
#     print("Afsuski, sizda chegirma yo'q")
# elif 50000 <= xarid_summasi <= 100000:
#     print("Sizga 5% chegirma berildi")
#     print("To'lanadigan summa: ", xarid_summasi - xarid_summasi * 0.05)
# elif 100000 < xarid_summasi:
#     print("Sizga 10% chegirma berildi")
#     print("To'lanadigan summa: ", xarid_summasi - xarid_summasi * 0.1)
# else:
#     print("Noto'g'ri qiymat kiritdingiz")


# # <=== 3 - masala ===>
# login = input("Loginingizni kiriting: ")
# passwd = input("Parolingizni kiriting: ")

# if login == 'admin' and passwd == '12345':
#     print("Xush kelibsiz, admin!")
# else:
#     print("Login yoki parol xato")


# # <=== 4 - masala ===>
# yosh = int(input("Yoshingizni kiriting: "))

# if 0 < yosh < 13:
#     print("Sizga ushbu film tavsiya etilmaydi")
# elif 13 <= yosh < 18:
#     print("Siz filmni ota-onangiz bilan ko'rishingiz mumkin")
# elif yosh >= 18:
#     print("Siz filmni tomosha qilishingiz mumkin")
# else:
#     print("Noto'g'ri yosh kiritildi")


# # <=== 5 - masala ===>
# print("Menyu: \n1. Osh \n2. Mastava \n3. Shashlik")
# taom_raqami = int(input("Taom raqamini kiriting: "))

# if taom_raqami == 1:
#     print("Siz Oshni tanladingiz. Bu taom 60-90 daqiqa oralig'ida tayyor bo'ladi. Narxi 25000 so'm")
# elif taom_raqami == 2:
#     print("Siz Mastavani tanladingiz. Bu taom 45-60 daqiqa oralig'ida tayyor bo'ladi. Narxi 20000 so'm")
# elif taom_raqami == 3:
#     print("Siz Shashlikni tanladingiz. Bu taom 60-75 daqiqa oralig'ida tayyor bo'ladi. Narxi 25000 so'm")
# else:
#     print("Iltimos menyudan tanlang")


# # <=== 6 - masala ===>
# email = input("Emailingizni kiriting: ")

# if email.find('@') == -1 or email.find('.com') == -1:
#     print("Noto'g'ri email manzili kiritildi")
# else:
#     print("Email qabul qilindi")


# # <=== 7 - masala ===>
# ball = int(input("Ballingizni kiriting:"))

# if 86 <= ball <= 100:
#     print("5 baho")
# elif 70 <= ball < 86:
#     print("4 baho")
# elif 55 <= ball < 70:
#     print("3 baho")
# elif ball < 55:
#     print("2 baho")
# else:
#     print("Noto'g'ri ball kiritildi")


# # <=== 8 - masala ===>
# card_sum = int(input("Kartangizdagi pul miqdorini kiriting: "))
# yechiladigan_sum = int(input("Yechiladigan pul miqdorini kiriting: "))

# if yechiladigan_sum > card_sum:
#     print("Hisobda yetarli mablag' mavjud emas")
# elif yechiladigan_sum < 5000:
#     print("Minimal yechish summasi 5 000 so'm")
# else:
#     print("Pul muvaffaqiyatli yechildi")
#     print(f"Kartangizda {card_sum - yechiladigan_sum} so'm mablag' qoldi")


# # <=== 9 - masala ===>
# kun = input("Bugun qaysi hafta kuni: ").capitalize()

# if kun == 'Dushanba' or kun == 'Seshanba' or kun == 'Chorshanba' or kun == 'Payshanba' or kun == 'Juma':
#     print("Bugun ish kuni")
# elif kun == 'Yakshanba' or kun == 'Shanba':
#     print("Bugun dam olish kuni")
# else:
#     print("Bunday hafta kuni mavjud emas")


# # <=== 10 - masala ===>
# trafik = int(input("Oyiga qancha internet trafik sarflaysiz(GB da): "))

# if 0 < trafik < 1:
#     print("Sizga 'Mini' tarifi mos keladi")
# elif 1 <= trafik <= 5:
#     print("Sizga 'Standard' tarifi mos keladi")
# elif 5 < trafik:
#     print("Sizga 'Unlimited' tarifi mos keladi")
# else:
#     print("Noto'g'ri ma'lumot kiritildi")