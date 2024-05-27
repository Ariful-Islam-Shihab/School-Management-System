from School import *
from ClassRoom import ClassRoom
from Subject import Subject
from Teacheer import Teacher
from Student import Student

school = School("ABC", "Dhaka")

# Adding Classroom
eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")


# Adding Student
rahim = Student("Rahim", eight)
karim = Student("Karim", nine)
fahim = Student("Fahim", ten)
hamim = Student("Hamim", ten)

# Adding Teachers
abul = Teacher("Abul Khan")
babul = Teacher("Babul Khan")
kabul = Teacher("Kabul Khan")


# Adding Subjects
bangla = Subject("Bangla", abul)
physics = Subject("Physics", babul)
chemistry = Subject("Chemistry", kabul)
biology = Subject("Biology", kabul)

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(chemistry)
nine.add_subject(biology)
nine.add_subject(physics)
nine.add_subject(chemistry)
ten.add_subject(chemistry)
ten.add_subject(physics)
ten.add_subject(bangla)
ten.add_subject(biology)

school.student_admission(rahim)
school.student_admission(karim)
school.student_admission(fahim)
school.student_admission(hamim)



school.add_teacher(bangla)
school.add_teacher(physics)
school.add_teacher(biology)
school.add_teacher(chemistry)

eight.take_semester_final()
nine.take_semester_final()
ten.take_semester_final()

print(school)