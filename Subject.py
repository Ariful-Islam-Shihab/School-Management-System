
class Subject:
    def __init__(self,name,teacher) -> None:
        self.max_marks=100
        self.name=name
        self.teacher=teacher
        self.pass_marks=33

    def exam(self,students):
        print("--------------Conducting Exam--------------")
        for stu in students:
            mark=self.teacher.evaluate_exam()
            stu.marks[self]=mark
        
