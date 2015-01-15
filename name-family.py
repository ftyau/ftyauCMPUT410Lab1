class Student:
    courseMarks = {}
    name = ""
    def __init__(self, name, family):
        self.name = name
        self.family = family

    def addCourseMark(self, course, mark):
        self.courseMarks[course] = mark

    def average(self):
        return float(sum(student1.courseMarks.values())) / \
               float(len(student1.courseMarks.values()))


student1 = Student("John", "Smith")
student1.addCourseMark("CMPUT410", 100)
student1.addCourseMark("CMPUT401", 85)
student1.addCourseMark("CMPUT301", 70)
student1.addCourseMark("CMPUT325", 50)

print("Name:", student1.name + " " + student1.family)
print("Courses and marks:", student1.courseMarks.items())
print("Average:", student1.average())
