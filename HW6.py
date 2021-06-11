

def average_mark_student(student_list, cours):
    average_mark = []
    for student in student_list:
        if cours in student.grades:
            average_mark += student.grades.get(cours)
    return sum(average_mark) / len(average_mark)


def average_mark_lector(lector_list, cours):
    average_mark = []
    for lector in lector_list:
        if cours in lector.grades:
            average_mark += lector.grades.get(cours)
    return sum(average_mark) / len(average_mark)


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_lc(self, lecture, course, grade):

        if isinstance(lecture, Lectures) and course in self.courses_in_progress and course in lecture.courses_attached:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_mark(self):
        return sum([sum(i) for i in self.grades.values()]) / sum([len(i) for i in self.grades.values()])

    def __lt__(self, other):
        return self.average_mark() < other.average_mark()

    def __str__(self):
         return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за дз: {self.average_mark()}\nКурсы в процессе изучения:{self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lectures(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def average_mark(self):
        return sum([sum(j) for j in self.grades.values()]) / sum([len(j) for j in self.grades.values()])

    def __lt__(self, other):
        return self.average_mark() < other.average_mark()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_mark()}'


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


student_m = Student('Drako', 'Malfoy', 'M')
student_m.courses_in_progress += ['Python']
student_m.finished_courses += ['Java']

student_f = Student('Hermi', 'Greynger', 'F')
student_f.courses_in_progress += ['Python']
student_f.finished_courses += ['Golang']

reviewer_m = Reviewer('Severus', 'Snape')
reviewer_m.courses_attached += ['Python']

reviewer_f = Reviewer('Minerva', 'McGonagall')
reviewer_f.courses_attached += ['Python']

lector_m = Lectures('Volan', 'Demort')
lector_m.courses_attached += ['Python']

lector_f = Lectures('Belatrisa', 'Leinstreing')
lector_f.courses_attached += ['Python']

reviewer_f.rate_hw(student_f, 'Python', 4)
reviewer_f.rate_hw(student_m, 'Python', 10)
reviewer_m.rate_hw(student_f, 'Python', 8)
reviewer_m.rate_hw(student_m, 'Python', 9)

student_f.rate_lc(lector_m, 'Python', 8)
student_f.rate_lc(lector_f, 'Python', 5)
student_m.rate_lc(lector_m, 'Python', 10)
student_m.rate_lc(lector_f, 'Python', 10)

student_list = [student_m, student_f]
student_average_mark = average_mark_student(student_list, 'Python')
lector_average_mark = average_mark_lector([lector_m, lector_f], 'Python')


print('******')
print(student_m)
print('******')
print(student_f)
print('******')
print(reviewer_f)
print('******')
print(reviewer_m)
print('******')
print(lector_m)
print('******')
print(lector_f)
print('******')
print(lector_m < lector_f)
print('******')
print(student_m > student_f)
print('******')
print(f'Средняя оценка студентов: {student_average_mark}')
print(f'Средняя оценка предователей: {lector_average_mark}')

