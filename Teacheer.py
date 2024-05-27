
from Person import Person
import random


class Teacher(Person):
    def __init__(self, name) -> None:
        super().__init__(name)

    def teach():
        print("Teaching")
    def evaluate_exam(self):
        return random.randint(a=0,b=100)
    