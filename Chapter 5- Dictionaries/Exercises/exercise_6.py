

students = []

Honor_students = {
    'student grade': '90',
    'student name': 'Raven',
}
students.append(Honor_students)

Honor_students = {
    'student grade': '94',
    'student name': 'Paula',
}
students.append(Honor_students)

Honor_students = {
    'student grade': '86',
    'student name': 'Andrei',
}
students.append(Honor_students)



for Honor_students in students:
    print("\nHonor students in class :")
    for key, value in Honor_students.items():
        print("\t" + key + ": " + str(value))