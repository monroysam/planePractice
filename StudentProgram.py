import StudentClass as s

import datetime

def main():
    student_ID = input("Enter your ID: ")
    student_name = input("Enter your name: ")
    student_DOB = input("Enter DOB in 'XX/XX/XXXX' :")
    student_class = input("Enter your class: ").title()

    #create instance
    stud = s.Student(student_ID, student_name, student_DOB, student_class)

    stud.calc_age()
    stud.get_registration()

    print()
    print(stud)

main()