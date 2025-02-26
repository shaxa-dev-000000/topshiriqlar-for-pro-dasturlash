# Import Modules ==============>
from set_question import section1
from colors import cyan, clear


# Main Module =============>
while True:
    print(cyan + "Kim milliarder bo'lishni xohlaydi o'yiniga xush kelibsiz!")
    print("""
    Buyruqni tanlang:
        1 - o'yinni boshlash
        2 - natijalarni ko'rish

        0 - o'yindan chiqish
        * - konsolni tozalash""" + clear)

    section = input("        -> ")
    if section == "1":
        section1()
    elif section == "2":
        pass
    elif section == "0":
        break
    elif section == "*":
        pass
    else:
        print("Noto'g'ri buyruq kiritildi!")
