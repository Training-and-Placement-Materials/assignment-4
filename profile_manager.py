"""
Name: Areeb Khan
Enrollment: 0103CS231080
Batch: 6
Batch Time: 12:10 to 13:50
Assignment: 3
"""
# Importing User Modules
import console as C
import database_manager as dbmgr
import quiz as Q
# Importing Modules
import time

format = (
    "password",
    "First Name",
    "Middle Name",
    "Last Name",
    "Branch",
    "Enrollment",
    "Roll No",
    "Phone No",
    "E-Mail",
    "Address",
    "Pincode"
)

# Student Database
student_db = dbmgr.db_load()

# Logged-In User's data
logged_user = ""
logged = False

def register():
    while True:
        uname = input("Username: ").lower()
        if(uname in student_db.keys()):
            C.write("This user name already exists. Try Again.")
            continue

        password = input("Password: ")
        break
    
    while True:
        C.clear()
        C.write("Enter details for "+uname)
        first_name = input("First name: ")
        middle_name = input("Middle Name: ")
        last_name = input("Last Name: ")
        
        branch = input("Branch (CS|ES|AD|ME|CE): ")
        
        if(branch not in ["CS", "EC", "AD", "ME", "CE"]):
            C.write("Invalid Branch.")
            continue
        
        enrollment = input("Enrollment No: ")
        if(branch not in enrollment):
            C.write("Branch does not match based on enrollment.")
            continue

        roll = int(input("Roll No: "))
        phone_no = int(input("Phone No: "))
        email = input("Email: ")
        address = input("Address: ")
        pincode = int(input("Pincode: "))


        choice = input("Are these details correct?[y]: ").lower()
        if(choice == "y"):
            student_db[uname] = {
                "password": password,
                "first_name": first_name,
                "middle_name": middle_name,
                "last_name": last_name,
                "branch": branch,
                "enrollment": enrollment,
                "roll": roll,
                "phone_no": phone_no,
                "email": email,
                "address": address,
                "pincode": pincode,
                "Quiz Marks": 0
            }
            dbmgr.db_write(student_db)
            break

def login():
    global logged_user, logged
    print("-"*20)
    C.write("Enter credentials.")
    log_uname = input("Username: ").lower()
    if(log_uname in student_db):
        log_password = input("Password: ")
        if(log_password == student_db[log_uname]["password"]):
            logged_user = log_uname
            logged = True
            print("Logging in..")
        else:
            print("Wrong Password!")
    elif(log_uname == "admin"):
        log_password = input("Password: ")
        if(log_password == "1234"):
            logged_user = log_uname
            logged = True
            print("Logging in..")
        else:
            print("Wrong Password!")
    else:
        print("User does not exist!")
    time.sleep(2)

def show_profile():
    if(logged):
        C.clear()
        temp = list(student_db[logged_user].values())
        C.write(temp[1]+"'s Profile")
        print("-"*20)
        for i in range(1, 11):
            print(f"{format[i]}: {temp[i]}")
        input("Press enter to go back.")
    else:
        print("User not logged in.")
        time.sleep(2)

def update_profile():
    global student_db
    if(logged):
        C.clear()

        temp = list(student_db[logged_user].values())
        keys = list(student_db[logged_user].keys())
        C.write("Select entry you want to update.")
        for i in range(1, 10):
            print(f"{i}. {format[i]}: {temp[i]}")
        option = input("Select option(1-10): ")
        print("-"*20)
        
        if(option in "1234567891011"):
            option = int(option)
        
        if(option in [1, 2, 3, 8, 9]):
            temp_str = input(f"Enter {format[option]}: ")
            student_db[logged_user][keys[option]] = temp_str
            C.write("Updated.")
        elif(option == 4):
            temp_str = input("Enter Branch (CS|ES|AD|ME|CE): ")
            if(temp_str not in ["CS", "EC", "AD", "ME", "CE"]):
                C.write("Invalid Branch.")
            else:
                student_db[logged_user][keys[option]] = temp_str
                C.write("Updated Branch.")
        elif(option == 5):
            temp_str = input("Enter Enrollment No: ")
            if(temp[4] not in temp_str):
                C.write("Branch does not match based on enrollment. Update Branch first.")
            else:
                student_db[logged_user][keys[option]] = temp_str
                C.write("Updated Enrollment No.")
        elif(option in [6, 7,10]):
            temp_int = input(f"Enter {format[option]}: ")
            student_db[logged_user][keys[option]] = temp_int
            C.write("Updated.")
        else:
            C.write('Invalid Option.')
        dbmgr.db_write(student_db)
    else:
        print("User not logged in.")
    time.sleep(2)

def quiz():
    category, score, time_string = Q.start_quiz()

    C.clear()
    if(score > student_db[logged_user]["quiz"][category][0]):
        student_db[logged_user]["quiz"][category] = [score, time_string]
        dbmgr.db_write(student_db)
        C.write("Quiz Completed. New Highscore("+str(score)+")")
        time.sleep(2)

def quiz_results():
    C.clear()
    C.write("Enrollment No.   Category    Marks/Total    Datetime")
    for profile in student_db.values():
        enrollment = profile["enrollment"]
        for category, details in profile["quiz"].items():
            if(details[1]):
                print(f"{enrollment}\t {category}\t\t {details[0]}\t    {details[1]}")
    input("\nPress enter to go back.")

def logout():
    global logged_user, logged
    print("-"*20)
    choice = input("Do you really want to logout?[y]: ").lower()
    if(choice == "y"):
        logged_user = ""
        logged = False
        print("Logging out..")
    else:
        print("Going back to main menu.")
    time.sleep(2)