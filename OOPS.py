# Multiple Inheritance in Python
# Demonstrates method overriding and super()

class Student:
    def study(self):
        print("Student is studying ❤️")


class Info:
    def study(self):
        print("This is info")


class AIFTStudent(Info, Student):
    def study(self):
        print("AIFT student is studying")
        super().study()   # Calls study() of the first parent class (Info)

    def serious(self):
        print("AIFT students are studying seriously")


# -------- Object Creation --------
res = AIFTStudent()
res.study()
res.serious()
