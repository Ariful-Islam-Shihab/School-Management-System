
class ClassRoom:
    def __init__(self, name) -> None:
        self.name=name
        self.students=[]
        self.subjects=[]
    
    def add_student(self,student):
        roll_no=len(self.students)
        student.__id=roll_no
        self.students.append(student)

    def add_subject(self,subject):
        self.subjects.append(subject)

    def take_semester_final(self):
        print("\t********Semester Final*************")
        for i in self.subjects:
            i.exam(self.students)
        for i in self.students:
            i.calculate_final_grade()
    