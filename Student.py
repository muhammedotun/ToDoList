from Person import Person
from course import course

class Student(Person):
    """docstring for student."""

    def __init__(self, number, name, lastName):
        super().__init__(number, name , lastName)
        self.course = None
        self.email = self.name + '.' + self.lastName + "@email.com"


    def printStudent(self):
        print("number: " , self.number , " name:", self.fullName())


    def fullName(self):
        return '{} {}'.format(self.name, self.lastName)

    def addCourse(self, myCourse):
        if course.courseCapasity > 0:
            self.course = myCourse
            course.courseCapasity -= 1
            print(self.fullName(), "added of", self.course.courseName)

        else:
            print("the course is full")
