class Student:
    def __init__(self):
        self.Course_Name = ""
        self.Student_ID = []
        self.Student_Grade = []

    def add_info(self):
        self.Course_Name = input("What is the new course name? ")
        n = int(input("How many student IDs + student scores would you like to add to this new class? "))
        for x in range(0, n):
            self.Student_ID.append(input("What is the student's ID for this class? "))
            self.Student_Grade.append(input("What is the student's grade for this class? "))

    def display_info(self):
        print("Course name: ", self.Course_Name)
        print("Student ID: ", self.Student_ID)
        print("Student's grade: ", self.Student_Grade)
