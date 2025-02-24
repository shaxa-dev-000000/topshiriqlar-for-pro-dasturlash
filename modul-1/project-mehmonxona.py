print("Astrum Mehmonxonasiga xush kelibsiz!\n")

mehmonlar = {
    "shaxriyor": [8, "lyuks"],
    "bekzod": [10, "standart"]
}

def mehmonlarRoyxati():
    royxat = """Mehmon           Xona          Xona turi"""
    for i in mehmonlar:
        a = " " * (17 - len(i))
        b = " " * (14 - len(str(mehmonlar.get(i)[0])))
        mehmon = f"\n{i.capitalize()}{a}{mehmonlar.get(i)[0]}{b}{mehmonlar.get(i)[1]}"
        royxat += mehmon
    print(royxat, "\n")

def addNewMehmon():
    while True:
        ism = input("Ism kiriting: ")
        if len(ism) > 0:
            break
    while True:
        xona_raqami = input("Xona raqamini kiriting: ")
        if len(xona_raqami) > 0:
            for mehmon in mehmonlar:
                if int(xona_raqami) == mehmonlar.get(mehmon)[0]:
                    print("Bu xona band!")
                    break
            else:
                break


    while True:
        xona_turi = input("1 - Lyuks \n2 - Standart \n3 - Ekonom \n-> ")
        if xona_turi == "1":
            xona_turi = "lyuks"
            break
        elif xona_turi == "2":
            xona_turi = "standart"
            break
        elif xona_turi == "3":
            xona_turi == "ekonom"
            break
        else:
            print("Noto'g'ri buyruq kiritildi")

    mehmonlar[ism] = [int(xona_raqami), xona_turi]
    print("Mehmon qo'shildi\n")

def deleteMehmon():
    while True:
        mehmon = input("Kimni o'chirmoqchisiz :")
        if mehmon.lower() in mehmonlar:
            print(f"{mehmon} o'chirildi\n")
            del mehmonlar[mehmon]
            break
        else:
            print("Bunday mehmon topilmadi")


print("Bo'limni tanlang:")
while True:
    bolim = input("1 - Mehmon qo'shish \n2 - Mehmonni ro'yxatdan chiqarish \n3 - Ro'yxatni chiqarish \n0 - Chiqish \n-> ")

    if bolim == "1":
        addNewMehmon()
    elif bolim == "2":
        deleteMehmon()
    elif bolim == "3":
        mehmonlarRoyxati()
    elif bolim == "0":
        break
    else:
        print("Noto'g'ri buyruq kiritldi")


