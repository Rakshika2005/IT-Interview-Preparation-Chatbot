#!/usr/bin/env python3
###############################################################################
# IT INTERVIEW PREPARATION CHATBOT – SINGLE FILE PROJECT
# Author: Student Project Version
# Rounds: Aptitude | Coding | GD | HR (Voice)
###############################################################################

import time
import random
import speech_recognition as sr
import getpass
USE_VOICE = False   # Set True only on local machine
###############################################################################
# LOGIN SYSTEM
###############################################################################

users = {
    "admin": "admin123"
}

def register():
    print("\n📝 REGISTER NEW USER")
    username = input("Choose username: ")

    if username in users:
        print("❌ Username already exists")
        return False

    password = getpass.getpass("Password: ")
    users[username] = password
    print("✅ Registration successful")
    return True
def login():
    print("\n🔐 LOGIN")
    attempts = 3

    while attempts > 0:
        username = input("Username: ")
        password = getpass.getpass("Password: ")  # 🔐 Hidden password

        if users.get(username) == password:
            print(f"\n✅ Welcome {username}!")
            return username
        else:
            attempts -= 1
            print(f"❌ Invalid credentials ({attempts} attempts left)")

    print("\n🚫 Too many failed attempts. Exiting...")
    exit()



###############################################################################
# GLOBAL DATA
###############################################################################

candidate_name = ""
dashboard = {}

###############################################################################
# TIMER FUNCTION
###############################################################################

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"\r⏳ Time Left: {i} sec", end="")
        time.sleep(1)
    print("\n⏰ Time Over\n")

###############################################################################
# APTITUDE QUESTIONS (30 TOTAL)
###############################################################################

verbal_questions = [
    ("Synonym of 'Quick'", ["Slow", "Fast", "Lazy", "Weak"], 1),
    ("Antonym of 'Success'", ["Win", "Profit", "Failure", "Gain"], 2),
    ("Choose correct spelling", ["Recieve", "Receive", "Receeve", "Receve"], 1),
    ("Meaning of 'Brief'", ["Short", "Long", "Wide", "Big"], 0),
    ("Plural of 'Child'", ["Childs", "Children", "Childes", "Child"], 1),
    ("Fill blank: He ___ playing.", ["is", "are", "was", "were"], 0),
    ("One word for fear of heights", ["Hydrophobia", "Acrophobia", "Claustrophobia", "Arachnophobia"], 1),
    ("Synonym of 'Happy'", ["Sad", "Angry", "Joyful", "Weak"], 2),
    ("Antonym of 'Hot'", ["Cold", "Warm", "Heat", "Cool"], 0),
    ("Choose correct sentence", ["He go school", "He goes to school", "He going school", "He gone school"], 1)
]

quantitative_questions = [
    ("10 + 20 =", ["20", "25", "30", "40"], 2),
    ("15 × 2 =", ["20", "25", "30", "35"], 2),
    ("100 / 4 =", ["20", "25", "30", "40"], 1),
    ("Square root of 81", ["7", "8", "9", "10"], 2),
    ("20% of 200", ["20", "30", "40", "50"], 2),
    ("5² =", ["10", "20", "25", "30"], 2),
    ("LCM of 2 & 4", ["2", "4", "6", "8"], 1),
    ("50 – 15 =", ["25", "30", "35", "40"], 2),
    ("Simple interest of 1000 at 10%", ["100", "200", "300", "400"], 0),
    ("Average of 10 & 20", ["10", "15", "20", "25"], 1)
]

logical_questions = [
    ("Odd one out: Dog, Cat, Cow, Car", ["Dog", "Cat", "Cow", "Car"], 3),
    ("2, 4, 6, ?", ["7", "8", "9", "10"], 1),
    ("Day after Monday", ["Sunday", "Tuesday", "Wednesday", "Friday"], 1),
    ("A is to Z as 1 is to ?", ["25", "26", "27", "24"], 1),
    ("Opposite of North", ["South", "East", "West", "Up"], 0),
    ("Triangle sides?", ["2", "3", "4", "5"], 1),
    ("Find missing: A, C, E, ?", ["F", "G", "H", "I"], 1),
    ("Even number", ["3", "5", "7", "8"], 3),
    ("Clock has ___ hours", ["10", "11", "12", "13"], 2),
    ("If 1=3, 2=5, 3=?", ["6", "7", "8", "9"], 1)
]

###############################################################################
# APTITUDE ROUND
###############################################################################
random.shuffle(verbal_questions)
random.shuffle(quantitative_questions)
random.shuffle(logical_questions)

def aptitude_round():
    print("\n🧠 APTITUDE ROUND STARTED (3 Minutes)")
    score = 0
    start = time.time()

    for section in [verbal_questions, quantitative_questions, logical_questions]:
        for q, options, ans in section:

            # Stop round if 3 minutes completed
            if time.time() - start > 180:
                print("\n⏰ Time limit reached! Ending Aptitude Round...")
                feedback = "Time Over - Practice time management."
                dashboard["Aptitude"] = (score, feedback)
                print(f"\nScore: {score}/30")
                return

            remaining = 180 - int(time.time() - start)

            # Warning when time almost finished
            if remaining <= 20:
                print(f"\n⚠ WARNING: Only {remaining} seconds left!")

            print("\n" + "-" * 50)
            print(q)

            for i, opt in enumerate(options):
                print(f"{i+1}. {opt}")

            user_input = input("\nEnter your answer (1-4): ").strip()

            if user_input.isdigit():
                user = int(user_input) - 1
                if user == ans:
                    score += 1

            input("\n➡ Press Enter to go to next question...")

    feedback = "Excellent aptitude skills!" if score >= 22 else \
               "Good aptitude but needs practice." if score >= 15 else \
               "Weak aptitude – practice required."

    dashboard["Aptitude"] = (score, feedback)

    print("\n📌 APTITUDE ROUND COMPLETED")
    print(f"Score: {score}/30")
    print(f"Feedback: {feedback}")
    print("-" * 50)
###############################################################################
# CODING ROUND
###############################################################################

coding_questions = [
    "Reverse a string",
    "Check palindrome",
    "Factorial of a number",
    "Armstrong number check",
    "Prime number check",
    "Count vowels in string",
    "Reverse a list",
    "Find maximum element",
    "Sum of digits",
    "Swap two numbers"
]

def coding_round():
    print("\n💻 CODING ROUND STARTED (Expert Mode)")
    score = 0
    total = 10

    def take_code(signature):
        print("\nWrite function body (press ENTER on empty line to finish)")
        print(signature)
        lines = []
        while True:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)

        code = signature + "\n"
        for l in lines:
            code += "    " + l + "\n"
        return code

    # Shuffle questions for randomness
    random.shuffle(coding_questions)

    for q in coding_questions:
        print("\n" + "-" * 60)
        print("Question:", q)
        local_env = {}

        try:
            # 1 Reverse String
            if q == "Reverse a string":
                code = take_code("def reverse_string(s):")
                exec(code, {}, local_env)

                tests = [("abc", "cba"), ("hello", "olleh")]
                if all(local_env["reverse_string"](inp) == out for inp, out in tests):
                    score += 1
                    print("✅ Correct")
                else:
                    print("❌ Failed Test Cases")

            # 2 Palindrome
            elif q == "Check palindrome":
                code = take_code("def is_palindrome(s):")
                exec(code, {}, local_env)

                tests = [("madam", True), ("hello", False)]
                if all(local_env["is_palindrome"](inp) == out for inp, out in tests):
                    score += 1
                    print("✅ Correct")
                else:
                    print("❌ Failed Test Cases")

            # 3 Factorial
            elif q == "Factorial of a number":
                code = take_code("def factorial(n):")
                exec(code, {}, local_env)

                tests = [(5, 120), (3, 6)]
                if all(local_env["factorial"](inp) == out for inp, out in tests):
                    score += 1
                    print("✅ Correct")
                else:
                    print("❌ Failed Test Cases")

            # 4 Armstrong
            elif q == "Armstrong number check":
                code = take_code("def is_armstrong(n):")
                exec(code, {}, local_env)

                tests = [(153, True), (370, True), (123, False)]

                if "is_armstrong" in local_env:
                    try:
                        if all(local_env["is_armstrong"](inp) == out for inp, out in tests):
                            score += 1
                            print("✅ Correct")
                        else:
                            print("❌ Failed Test Cases")
                    except Exception as e:
                        print("❌ Runtime Error:", e)
                else:
                    print("❌ Function not defined properly")
           #5 Prime Check
            elif q == "Prime number check":
                code = take_code("def is_prime(n):")
                exec(code, {}, local_env)

                tests = [(7, True), (4, False)]
                if all(local_env["is_prime"](inp) == out for inp, out in tests):
                    score += 1
                    print("✅ Correct")
                else:
                    print("❌ Failed Test Cases")

            # 6 Count Vowels
            elif q == "Count vowels in string":
                code = take_code("def count_vowels(s):")
                exec(code, {}, local_env)

                tests = [("education", 5), ("sky", 0)]
                if all(local_env["count_vowels"](inp) == out for inp, out in tests):
                    score += 1
                    print("✅ Correct")
                else:
                    print("❌ Failed Test Cases")

            # 7 Reverse List
            elif q == "Reverse a list":
                code = take_code("def reverse_list(lst):")
                exec(code, {}, local_env)

                tests = [([1,2,3], [3,2,1]), ([5,6], [6,5])]
                if all(local_env["reverse_list"](inp) == out for inp, out in tests):
                    score += 1
                    print("✅ Correct")
                else:
                    print("❌ Failed Test Cases")

            # 8 Find Maximum
            elif q == "Find maximum element":
                code = take_code("def find_max(lst):")
                exec(code, {}, local_env)

                tests = [([1,5,2], 5), ([-1,-5,-2], -1)]
                if all(local_env["find_max"](inp) == out for inp, out in tests):
                    score += 1
                    print("✅ Correct")
                else:
                    print("❌ Failed Test Cases")

            # 9 Sum of Digits
            elif q == "Sum of digits":
                code = take_code("def sum_digits(n):")
                exec(code, {}, local_env)

                tests = [(123, 6), (45, 9)]
                if all(local_env["sum_digits"](inp) == out for inp, out in tests):
                    score += 1
                    print("✅ Correct")
                else:
                    print("❌ Failed Test Cases")

            # 10 Swap Numbers
            elif q == "Swap two numbers":
                code = take_code("def swap(a, b):")
                exec(code, {}, local_env)

                if local_env["swap"](3, 4) == (4, 3):
                    score += 1
                    print("✅ Correct")
                else:
                    print("❌ Failed Test Case")

        except Exception as e:
            print("❌ Code Error:", e)

        input("➡ Press Enter for next question...")

    feedback = (
        "🏆 Excellent coding skills!" if score >= 8 else
        "👍 Good coding skills." if score >= 5 else
        "⚠ Weak coding fundamentals – practice required."
    )

    dashboard["Coding"] = (score, feedback)

    print("\n📌 CODING ROUND COMPLETED")
    print(f"Score: {score}/{total}")
    print(f"Feedback: {feedback}")
###############################################################################
# DSA PRACTICE ROUND (ARRAYS | STRINGS | RECURSION)
###############################################################################
def dsa_round():
    print("\n📘 DSA PRACTICE ROUND STARTED")
    score = 0

    # ARRAY
    print("\nArray Question:")
    arr = input("Enter numbers separated by space: ")

    try:
        nums = list(map(int, arr.split()))
    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")
        dashboard["DSA"] = (0, "Invalid input")
        return

    # 👇 REPLACED BLOCK HERE
    if not nums:
        print("❌ No numbers entered")
        dashboard["DSA"] = (score, "Invalid input")
        return

    correct = max(nums)

    try:
        user_ans = int(input("Enter the maximum number: "))
    except ValueError:
        print("❌ Invalid number")
        dashboard["DSA"] = (score, "Invalid input")
        return

    if user_ans == correct:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer is {correct}")
    # STRING
    print("\nString Question:")
    s = input("Enter a string: ")

    rev = input("Enter reversed string: ").strip()

    if s[::-1] == rev:
        print("✅ Correct")
        score += 1
    else:
        print("❌ Wrong")
    # RECURSION
    print("\nRecursion Question:")

    try:
        n = int(input("Enter number: "))
    except ValueError:
        print("❌ Invalid number")
        dashboard["DSA"] = (score, "Invalid input")
        return

    def factorial(x):
        return 1 if x <= 1 else x * factorial(x - 1)

    try:
        user_fact = int(input("Enter factorial value: "))
    except ValueError:
        print("❌ Invalid factorial input")
        dashboard["DSA"] = (score, "Invalid input")
        return

    if user_fact == factorial(n):
        print("✅ Correct")
        score += 1
    else:
        print("❌ Wrong")
    feedback = (
        "Excellent DSA fundamentals!" if score == 3 else
        "Good DSA basics, needs practice." if score == 2 else
        "Weak DSA concepts – practice required."
    )

    dashboard["DSA"] = (score, feedback)

    print("\n📌 DSA ROUND COMPLETED")
    print(f"Score: {score}/3")
    print(f"Feedback: {feedback}")
    print("-" * 50)

###############################################################################
# GROUP DISCUSSION ROUND
###############################################################################

gd_topics = [
    "Artificial Intelligence replacing jobs",
    "Remote work future",
    "Social media impact",
    "Climate change",
    "Online education",
    "Data privacy",
    "Is coding mandatory for IT?"
]

def gd_round():
    print("\n🗣️ GROUP DISCUSSION ROUND")
    for i, topic in enumerate(gd_topics):
        print(f"{i+1}. {topic}")

    choice = input("Choose a topic number: ")
    print("Discuss your views (type minimum 40 words):")
    speech = input("Your answer: ")
    input("\nPress Enter to submit GD response...")

    score = 10 if len(speech.split()) >= 40 else 6 if len(speech.split()) >= 20 else 3

    feedback = "Excellent communication skills!" if score >= 8 else \
               "Average communication." if score >= 5 else \
               "Needs confidence & clarity."

    dashboard["Group Discussion"] = (score, feedback)
    print("\n📌 GROUP DISCUSSION ROUND COMPLETED")
    print(f"Score: {score}/10")
    print(f"Feedback: {feedback}")
    print("-" * 50)


###############################################################################
# HR VOICE ROUND
###############################################################################
# NOTE: Replit does not support microphone input.
# Voice input works only on local machine.

hr_questions = [
    "Tell me about yourself",
    "What are your strengths?",
    "What are your weaknesses?",
    "Why should we hire you?",
    "Where do you see yourself in five years?"
]

def listen_voice():
    if not USE_VOICE:
        return input("Type your answer: ")

    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("🎤 Speak now...")
            audio = recognizer.listen(source, timeout=5)
            return recognizer.recognize_google(audio)
    except:
        return input("Type your answer: ")

def hr_round():
    print("\n🎤 HR ROUND STARTED")
    score = 0

    for q in hr_questions:
        print("\n", q)
        ans = listen_voice()
        input("\nPress Enter for next HR question...")

        print("Captured:", ans)
        if len(ans.split()) >= 10:
            score += 2

    feedback = "Strong HR interview performance!" if score >= 8 else \
               "Good HR responses." if score >= 5 else \
               "Needs HR interview practice."

    dashboard["HR"] = (score, feedback)
    print("\n📌 HR ROUND COMPLETED")
    print(f"Score: {score}/10")
    print(f"Feedback: {feedback}")
    print("-" * 50)


###############################################################################
# FINAL DASHBOARD
###############################################################################

def final_dashboard():
    print("\n📊 FINAL INTERVIEW DASHBOARD")
    print(f"Candidate Name: {candidate_name}")
    print("-" * 50)

    total = 0
    for round_name in ["Aptitude", "Coding", "DSA", "Group Discussion", "HR"]:

        score, feedback = dashboard.get(round_name, (0, "Round not attempted"))
        print(f"{round_name} Score: {score}")
        print(f"Feedback: {feedback}\n")
        total += score

    print("TOTAL SCORE:", total)

    if total >= 35:
        print("✅ FINAL DECISION: YOU ARE ELIGIBLE TO BE HIRED")
    else:
        print("❌ FINAL DECISION: MORE PRACTICE REQUIRED")

###############################################################################
# MAIN FUNCTION
###############################################################################

def main():
    global candidate_name
    ###############################################################################
    # PROGRAM START
    ###############################################################################

    print("======================================")
    print(" IT INTERVIEW PREPARATION CHATBOT ")
    print("======================================")

    choice = input("\n1. Login\n2. Register\nChoose option: ")

    if choice == "2":
        register()

    candidate_name = login()   # 🔐 BLOCKS ACCESS UNTIL LOGIN SUCCESS

    aptitude_round()
    coding_round()
    dsa_round()
    gd_round()
    hr_round()
    final_dashboard()


if __name__ == "__main__":
    main()
