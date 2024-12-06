import Lab6Setup as LS
import pickle

CourseList = []
print("Use the list below.")
print("Please don't display without first adding.")
print(" ")
while 1:
    print("1. Add a course, student ID, and student grade")
    print("2. Display all courses, student IDs, and grades")
    print("3. Exit Program")
    option1 = int(input())

    if option1 == 1:
        s1 = LS.Student()  # create objects s1 and s2 for Student class
        s1.add_info()

        s2 = LS.Student()
        s2.add_info()

        s3 = LS.Student()
        s3.add_info()

        s4 = LS.Student()
        s4.add_info()

        s5 = LS.Student()
        s5.add_info()

    if option1 == 2:
        f=open('myStudent.dat', 'ab')  # write the objects s1 and s2 into a *.dat file
        pickle.dump(s1, f)
        pickle.dump(s2, f)
        pickle.dump(s3, f)
        pickle.dump(s4, f)
        pickle.dump(s5, f)
        f.close()
        # open the same dat file in read-binary mode
        f = open('myStudent.dat', 'rb')
        # use iterations to read the objects from the file and print the attributes of the class
        while 2:
            try:
                data = pickle.load(f)
                print(data.Course_Name)
                print(data.Student_ID)
                print(data.Student_Grade)
            except EOFError:
                break
        f.close()

    if option1 == 3:
        print("You have ended the program.")
        break