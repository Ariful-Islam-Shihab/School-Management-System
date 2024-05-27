
class School:
    def __init__(self,name,address) -> None:
        self.name=name
        self.address=address
        self.teachers={}
        self.classrooms={}
    def add_classroom(self,classroom):
        self.classrooms[classroom.name]=classroom
    
    
    def add_teacher(self,subject):
        self.teachers[subject.teacher]=subject

    def student_admission(self,student):
        classname=student.classroom.name
        onj=self.classrooms[classname]
        onj.add_student(student)

        
    @staticmethod
    def calculate_grade(marks):
        if marks>=90:
            return 4.00
        elif marks>=86:
            return 3.67
        elif marks>=81:
            return 3.33
        elif marks>=78:
            return 3.00
        elif marks>=55:
            return 1.00
        else:
            return 0.00
    
    
    @staticmethod
    def grade_to_value(grade):
        if grade>=4.00:
            return "A"
        elif grade>=3.67:
            return "B"
        elif grade>=3.33:
            return "C"
        elif grade>=3.00:
            return "D"
        elif grade>=1.00:
            return "E"
        else:
            return "F"
    @staticmethod
    def value_to_grade(marks):
        if marks>=90:
            return "A"
        elif marks>=86:
            return "B"
        elif marks>=81:
            return "C"
        elif marks>=78:
            return "D"
        elif marks>=55:
            return "E"
        else:
            return "F"
        
    def __repr__(self):
        print("----------------------------")
        print(self.name)
        print("Our Teachers")
        for i in self.teachers.keys():
            print(f"Name: {i.name}")
        print("----------------------------")
        print("Our Students")
        for i,j in self.classrooms.items():
            print()
            print(f"Class room: {i} ")
            print(f"Students: ")
            for k in j.students:
                print(k)
            

        return " "

        
