# Import Modules ==============>
from get_and_set.get_questions import get_question, get_answer
from data.colors import blue, red, yellow, clear
from get_and_set.get_results import get_result


# First section func. ============>
def section1():
    while True:
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
                print(yellow + f"Natija: {count}/10\n" + clear)
                get_result(name, count)

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
                pass
            else:
                print("Bunday variant yo'q")
