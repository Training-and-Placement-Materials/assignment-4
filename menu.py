"""
Name: Areeb Khan
Enrollment: 0103CS231080
Batch: 6
Batch Time: 12:10 to 13:50
Assignment: 3
"""
# Importing User Modules
import profile_manager as pmgr
import console as C

def screen():
    C.write("Welcome to LNCT")
    response = input("1. Registration\n2. Login\n3. Exit\nSelect option(1-3): ")
    if response == '1':
        pmgr.register()
    elif response == '2':
        pmgr.login()
    elif response == '3':
        C.write("Terminating..")
        exit()
    else:
        return "error"

def logged_in_screen():
    C.write("Welcome to LNCT, " + pmgr.student_db[pmgr.logged_user]["first_name"])
    response = input("1. Profile\n2. Update profile\n3. Take Quiz\n4. Logout\n5. Exit\nSelect option(1-5): ")

    if response == '1':
        pmgr.show_profile()
    elif response == '2':
        pmgr.update_profile()
    elif response == '3':
        pmgr.quiz()
    elif response == '4':
        pmgr.logout()
    elif response == '5':
        C.write("Terminating..")
        exit()
    else:
        return "error"

def admin_screen():
    C.write("ADMIN MENUE")
    response = input("1. Quiz Marks\n2. Logout\n3. Exit\nSelect option(1-3): ")

    if response == '1':
        pmgr.quiz_results()
    elif response == '2':
        pmgr.logout()
    elif response == '3':
        C.write("Terminating..")
        exit()
    else:
        return "error"

def menu():
    while True:
        C.clear()
        if(pmgr.logged_user == "admin"):
            log = admin_screen()
        elif(pmgr.logged):
            log = logged_in_screen()
        else:
            log = screen()
        if log == "error":
            continue
