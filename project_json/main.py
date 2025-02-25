# Import Modules ==============>
from get_questions import get_question, get_answer
import random


# Colors =============>
cyan = "\033[36m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
clear = "\033[0m"

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
        name = input("Ismingizni kiriting: ")
        quiz = get_question()
        answer = get_answer()
        count = 0
        help_chance = 1

        for i in range(10):
            a = next(quiz)
            b = next(answer)
            
            print(blue + f"{i + 1}-savol" + clear)
            print(a + "\n")
            print(f"a) {b[0]["key"]}")
            print(f"b) {b[1]["key"]}")
            print(f"c) {b[2]["key"]}")
            print(f"d) {b[3]["key"]}")
            print("h - yordam")
            input_ans = input("Javob: ")

            if input_ans == "a":
                if b[0]["isTrue"] != True:
                    break
                else:
                    count += 1
            elif input_ans == "b":
                if b[1]["isTrue"] != True:
                    break
                else:
                    count += 1
            elif input_ans == "c":
                if b[2]["isTrue"] != True:
                    break
                else:
                    count += 1
            elif input_ans == "d":
                if b[3]["isTrue"] != True:
                    break
                else:
                    count += 1
            elif input_ans == "h":
                if help_chance >= 1:
                    false_answers = [b[i]["key"] for i in range(4) if b[i]["isTrue"] != True]
                    del_answers = random.sample(false_answers, 2)
                    
            else:
                print("Bunday javob yo'q")

    elif section == "2":
        pass
    elif section == "0":
        break
    elif section == "*":
        pass
    else:
        print("Noto'g'ri buyruq kiritildi!")