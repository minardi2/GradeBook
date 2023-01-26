class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return print('ERROR')
    def avg_grades(self):
        sum_ = 0
        count = 0
        for enum_key, enum_value in self.grades.items():
            sum_ += sum(enum_value)
            count += len(enum_value)
        return sum_ / count
    def __str__(self):
        res = f'Name: {self.name}\nSurname: {self.surname}\nAverage rating for homework:{self.avg_grades()}\nCourses in process of studying: {self.courses_in_progress}\nFinished Courses: {self.finished_courses}'
        return res

    def __lt__(self, other):
        if isinstance(other, Student):
            if self.avg_grades() < other.avg_grades():
                return print(f'{self.name} {self.surname} has worse grades than {other.name} {other.surname}')
            else:
                return print(f'{other.name} {other.surname} has worse grades than {self.name} {self.surname}')
        else:
            return print('Error')


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grades(self):
        sum_ = 0
        count = 0
        for enum_key, enum_value in self.grades.items():
            sum_ += sum(enum_value)
            count += len(enum_value)
        return sum_ / count

    def __str__(self):
        res = f'Name: {self.name}\nSurname: {self.surname}\nAverage rating for courses: {self.avg_grades()}'
        return res

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            if self.avg_grades() < other.avg_grades():
                return print(f'{self.name} {self.surname} has worse grades than {other.name} {other.surname}')
            else:
                return print(f'{other.name} {other.surname} has worse grades than {self.name} {self.surname}')
        else:
            return print('Error')


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return print('ERROR')

    def __str__(self):
        res = f'Name: {self.name}\nSurname: {self.surname}'
        return res

student_andrei = Student('Andrei', 'Kozlov', 'M')
student_andrei.courses_in_progress += ['Python']
student_andrei.courses_in_progress += ['Git']
print(f'Student Name: {student_andrei.name} {student_andrei.surname}')

lecturer_anna = Lecturer('Anna', 'Karenina')
lecturer_anna.courses_attached += ['Python']
lecturer_anna.courses_attached += ['Git']
print(f'Lecturer Name: {lecturer_anna.name} {lecturer_anna.surname}')

reviewer_lisa = Reviewer('Lisa', 'Monroe')
reviewer_lisa.courses_attached += ['Python']
reviewer_lisa.courses_attached += ['Git']
print(f'Reviewer Name: {reviewer_lisa.name} {reviewer_lisa.surname}')

reviewer_lisa.rate_hw(student_andrei, 'Git', 9)
reviewer_lisa.rate_hw(student_andrei, 'Python', 10)
reviewer_lisa.rate_hw(student_andrei, 'Python', 10)
reviewer_lisa.rate_hw(student_andrei, 'Python', 10)

print(student_andrei.grades)

student_andrei.rate_hw(lecturer_anna, 'Python', 8)
student_andrei.rate_hw(lecturer_anna, 'Git', 10)
student_andrei.rate_hw(lecturer_anna, 'Git', 10)
print(lecturer_anna.grades)

lecturer_maria = Lecturer('Maria', 'Juk')
lecturer_maria.courses_attached += ['Python']
lecturer_maria.courses_attached += ['Git']
student_andrei.rate_hw(lecturer_maria, 'Python', 8)
student_andrei.rate_hw(lecturer_maria, 'Git', 9)
student_andrei.rate_hw(lecturer_maria, 'Git', 9)

student_kolia = Student('Kolia', 'Brabus', 'M')
student_kolia.courses_in_progress += ['Python']
student_kolia.courses_in_progress += ['Git']
reviewer_lisa.rate_hw(student_kolia, 'Git', 9)
reviewer_lisa.rate_hw(student_kolia, 'Python', 10)
reviewer_lisa.rate_hw(student_kolia, 'Python', 10)
reviewer_lisa.rate_hw(student_kolia, 'Python', 2)

print(reviewer_lisa)
print(lecturer_anna)
print(student_andrei)

lecturer_anna.__lt__(lecturer_maria)
student_andrei.__lt__(student_kolia)

students = [student_andrei, student_kolia]
lecturers = [lecturer_anna, lecturer_maria]

def average_grades_stud(students, name):
    total = 0
    count_ = 0
    for student in students:
        for key, values in student.grades.items():
            if key == name:
                total += sum(values)
                count_ += len(values)
    return total / count_

print(f"Average grade of students who learn Python - {average_grades_stud(students, 'Python')}")

def average_grades_lect(lecturers, name):
    total = 0
    count_ = 0
    for lecturer in lecturers:
        for key, values in lecturer.grades.items():
            if key == name:
                total += sum(values)
                count_ += len(values)
    return total / count_

print(f"Average grade of teachers who teach Python - {average_grades_lect(lecturers, 'Python')}")