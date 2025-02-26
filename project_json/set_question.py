# Import Modules ==============>
from get_questions import get_question, get_answer
from colors import blue, red, yellow, clear


def section1():
    name = input("Ismingizni kiriting: ")
    quiz = get_question()
    answer = get_answer()
    count = 0
#    help_chance = 1

    for i in range(10):
        a = next(quiz)
        b = next(answer)

        print(blue + f"\n{i + 1}-savol" + clear)
        print(a + "\n")
        print(f"a) {b[0]["key"]}")
        print(f"b) {b[1]["key"]}")
        print(f"c) {b[2]["key"]}")
        print(f"d) {b[3]["key"]}")
        print("h - yordam")
        input_ans = input("Javob: ")

        def for_info():
            print(red + "Noto'g'ri javob")
            print(blue + f"Ishtirokchi: {name}")
            print(yellow + f"Natija: {count}/10\n")

        if input_ans == "a":
            if b[0]["isTrue"] != True:
                for_info()
                break
            else:
                count += 1
        elif input_ans == "b":
            if b[1]["isTrue"] != True:
                for_info()
                break
            else:
                count += 1
        elif input_ans == "c":
            if b[2]["isTrue"] != True:
                for_info()
                break
            else:
                count += 1
        elif input_ans == "d":
            if b[3]["isTrue"] != True:
                for_info()
                break
            else:
                count += 1
        elif input_ans == "h":
            # if help_chance >= 1:
            #     false_answers = [b[i] for i in range(4) if b[i]["isTrue"] != True]
            #     del_answers = random.sample(false_answers, 2)
            #     b = [i for i in b if i not in del_answers]

            #     while True:
            #         print(blue + f"{i + 1}-savol" + clear)
            #         print(a + "\n")
            #         print(f"a) {b[0]["key"]}")
            #         print(f"b) {b[1]["key"]}")
            #         input_ans_2 = input("Javob: ")

            #         if input_ans_2 == "a":
            #             if b[0]["isTrue"] != True:
            #                 break
            #             else:
            #                 count += 1
            #                 help_chance -= 1
            #             break
            #         elif input_ans_2 == "b":
            #             if b[1]["isTrue"] != True:
            #                 break
            #             else:
            #                 count += 1
            #                 help_chance -= 1
            #             break
            #         else:
            #             print("Bunday variant yo'q")
            # else:
            #     print("sizda yordam qolmadi")
            pass
        else:
            print("Bunday variant yo'q")
