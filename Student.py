from School import School
from Person import Person



class Student(Person):
    def __init__(self, name,classroom) -> None:
        super().__init__(name)
        self.classroom=classroom
        self.marks={}
        self.subject_grade={}
        self.grade=0
        self.__id=None
    
    def calculate_final_grade(self):
        grade=0
        i=0
        for sub,mark in self.marks.items():
            i+=1
            grade=School.calculate_grade(mark)
            self.subject_grade[sub]=grade
            self.grade+=grade
        self.grade/=i
        return self.grade
    

    @property
    def getter(self):
        return self.__id
    

    @property
    def setter(self,id):
        self.id=id
    
    def __repr__(self) -> str:
        return f"Name: {self.name} ID: {self.__id} Grade:{self.grade}"