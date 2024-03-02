import datetime

class Student:

    def __init__(self, id, name, DOB, classification):
        self.__studentID = id
        self.__name = name
        self.__birth = DOB
        self.__classification = classification
        self.__age = 0
        self.__reg_date = 0

    #get and return
    def get_studentID(self, ident):
        self.__studentID = ident

    def return_studentID(self):
        return self.__studentID
    
    def get_name(self, name):
        self.__name = name

    def return_name(self):
        return self.__name
    
    def get_birth(self, DOB):
        self.__birth = DOB

    def return_name(self):
        return self.__birth 

    def get_classification(self, classification):
        self.__classification = classification

    def return_classification(self):
        return self.__classification
    
    #calculate age
    def calc_age(self):
        today = datetime.datetime.now().year
        splitdate = self.__birth.split('/')
        self.__age = today - int(splitdate[2])
        return self.__age

    #claculate registration
    def get_registration(self):
        if self.__classification == "Senior":
            self.__reg_date = "4/1 - 4/3"
        elif self.__classification == "Junior":
            self.__reg_date = "4/4 - 4/6"
        elif self.__classification == "Sophomore":
            self.__reg_date = "4/7 - 4/9"
        elif self.__classification == "Freshman":
            self.__reg_date = "4/10 - 4/12"
        else:
            self.__reg_date = "Error in calculating date"

    def __str__(self):
        return (f"Student ID: {format(self.__studentID)}\n"
        f"Student name: {format(self.__name)}\n"
        f"Student DOB: {format(self.__birth)}\n"
        f"Student class: {format(self.__classification)}\n"
        f"Student age: {format(self.__age)}\n"
        f"Registration date: {format(self.__reg_date)}")

    