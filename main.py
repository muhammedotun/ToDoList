from Student import Student
from Teacher import Teacher
from course import course

class main:
    # crate teacher and course

    muhammedotun = Teacher(1,"muhammed", "Ötün")
    python101 = course("python101", muhammedotun, 3)

    # crate teacher and course

    # crate list
    studentList = []
    # create list


    def addStudent(studentList, stdNumber, stdName, stdLastName):
        studentList.append(Student(stdNumber,stdName,stdLastName))

    def printStudentList(studentList):
        for student in studentList:
            student.printStudent()

    addStudent(studentList, 1, "emirhan", "eren")
    addStudent(studentList, 2, "yahya furkan", "kılıçoğlu")
    addStudent(studentList, 3, "onur", "kerim")
    addStudent(studentList, 4, "kasım", "eren")

    printStudentList(studentList)

    studentList[0].addCourse(python101)

    print(help(Student))
if __name__ == '__main__':
    main()
