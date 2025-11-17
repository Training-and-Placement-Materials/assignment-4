"""
Name: Areeb Khan
Enrollment: 0103CS231080
Batch: 6
Batch Time: 12:10 to 13:50
Assignment: 3
"""
# Importing User Modules
import console as C
# Importing Modules
import time, json, random, datetime

def select_category_menu():
    while True:
        C.clear()
        C.write("Select category for quiz")
        print("1. DSA\n2. DBMS\n3. Python")
        option = input("Select your Answer(1-3): ")

        if(option == '1'):
            return "DSA"
        elif(option == '2'):
            return "DBMS"
        elif(option == '3'):
            return "Python"
        else:
            continue

def load_questions(category):
    with open("questionnaire.json", "r") as j:
        questionair = json.load(j)
    return questionair[category]

def quiz_menu(no, question, option1, option2, option3, option4):
    while True:
        C.write("Question "+str(no)+": "+question)
        print(f"\n1. {option1}\n2. {option2}\n3. {option3}\n4. {option4}")
        option = input("Select your Answer(1-4): ")

        if option in ('1', '2', '3', '4'):
            return("Option_"+option)
        else:
            continue

def start_quiz():
    score = 0
    count = 1
    category = select_category_menu()
    questions = load_questions(category)
    
    while(len(questions) > 0):
        C.clear()
        quest = questions.pop(random.randint(0, len(questions)-1))
        user_answer = quiz_menu(count, quest["Question"], quest["Option_1"], quest["Option_2"], quest["Option_3"], quest["Option_4"])
        
        print("-"*25)
        if(quest["Answer"] == user_answer):
            score += 1
            C.write("Correct Answer! Score: "+str(score))
            count += 1
        else:
            C.write("Wrong Answer. Score: "+str(score))
            count += 1
        time.sleep(2)
    
    time_object = datetime.datetime.now()
    time_string = time_object.strftime("%d-%m-%y %H:%M:%S")
    return category, score, time_string