import numpy as np

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    # Добавление курса
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)


    # Оценка лектора
    def rate_lecturer(self, lecturer, course, lecture_grades):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.finished_courses:
            if course in lecturer.lecture_grades:
                lecturer.lecture_grades[course] += [lecture_grades]
            else:
                lecturer.lecture_grades[course] = [lecture_grades]
        else:
            return 'Ошибка'


    # Переопределение str
    def __str__(self):
        mean_grade = np.array(list(self.grades.values())).mean()
        res = f'\nСтуденты___\nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {mean_grade}\n'\
            f'Курсы в процессе изучения: '\
            f' {self.courses_in_progress} \n'\
            f'Завершенные курсы: {self.finished_courses}'
        return res


    # Сравнение студентов
    def __lt__(self, other):
        mean_grade_self = np.array(list(self.grades.values())).mean()
        mean_grade_other = np.array(list(other.grades.values())).mean()
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return mean_grade_self < mean_grade_other


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_grades = {}

    # Переопределяем str
    def __str__(self):
        mean_grade = np.array(list(self.lecture_grades.values())).mean()
        res = f'\nЛекторы___\nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {mean_grade}'
        return res

    # Переопределяем less than
    def __lt__(self, other):
        mean_grade_self = np.array(list(self.lecture_grades.values())).mean()
        mean_grade_other = np.array(list(other.lecture_grades.values())).mean()
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return mean_grade_self < mean_grade_other


class Reviewer(Mentor):

    # Метод выставления оценки за домашнее задание
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Переопределяем str
    def __str__(self):
        res = f'\nПроверющие___\nИмя: {self.name} \nФамилия: {self.surname}'
        return res


# Создаем экземпляр студента 1
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Music']
best_student.finished_courses += ['Dance']

# Создаем экземпляр студента 2
second_best_student = Student('Truto', 'Tuu', 'your_gender')
second_best_student.courses_in_progress += ['Python']
second_best_student.courses_in_progress += ['Music']
second_best_student.finished_courses += ['Dance']

# Создаем Ментора для задания 1
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']


# Создаем ревьюера
great_reviewer = Reviewer('Boss', 'Hugo')
great_reviewer.courses_attached += ['Python']
great_reviewer.courses_attached += ['Music']


# Ревьюер ставит оценки первому и второму студентам по Питону и по Музыке
great_reviewer.rate_hw(best_student, 'Python', 1)
great_reviewer.rate_hw(best_student, 'Python', 5)
great_reviewer.rate_hw(best_student, 'Python', 9)
great_reviewer.rate_hw(second_best_student, 'Python', 2)
great_reviewer.rate_hw(second_best_student, 'Python', 6)
great_reviewer.rate_hw(second_best_student, 'Python', 10)
great_reviewer.rate_hw(best_student, 'Music', 5)
great_reviewer.rate_hw(best_student, 'Music', 6)
great_reviewer.rate_hw(best_student, 'Music', 7)
great_reviewer.rate_hw(second_best_student, 'Music', 8)
great_reviewer.rate_hw(second_best_student, 'Music', 9)
great_reviewer.rate_hw(second_best_student, 'Music', 10)


# Создаем двух лекторов
wise_lecturer = Lecturer('Asta', 'Lavista')
wise_lecturer.courses_attached += ['Dance']
evenwiser_lecturer = Lecturer('Mon', 'Senior')
evenwiser_lecturer.courses_attached += ['Dance']


# Ставим лекторам оценки
best_student.rate_lecturer(wise_lecturer, 'Dance', 3)
best_student.rate_lecturer(wise_lecturer, 'Dance', 2)
best_student.rate_lecturer(wise_lecturer, 'Dance', 1)
best_student.rate_lecturer(evenwiser_lecturer, 'Dance', 4)
best_student.rate_lecturer(evenwiser_lecturer, 'Dance', 5)
best_student.rate_lecturer(evenwiser_lecturer, 'Dance', 6)


# Выводим результат
print(great_reviewer)
print(wise_lecturer)
print(second_best_student)
print(f'\nСравнение студентов и лекторов:')
print(evenwiser_lecturer > wise_lecturer)
print(best_student > second_best_student)


# Средняя оценка всех студентов за курс
class University():
    def __init__(self):
        self.student_list = []
        self.lecturer_list = []


    # Добавление студентов в список учащихся
    def add_student(self, student):
        self.student_list.append(student)


    # Добавление лекторов в список лекторов
    def add_lecturer(self, lecturer):
        self.lecturer_list.append(lecturer)


    # Метод подсчета средней оценки студента за курс
    def combine_grades_list(self, course):
        all_grades = {}
        for student in self.student_list:
            for k, v in student.grades.items():
                if k == course:
                    if k not in all_grades.keys():
                        all_grades.setdefault(k, v)
                    else:
                        all_grades[k] = list(all_grades[k] + v)

        mean_all_grades = np.array(list(all_grades.values())).mean()
        print(f'\nСредняя оценка всех студентов за курс "{course}": {mean_all_grades}')


    # Средняя оценка всех лекторов за курс
    def lecturers_grades_list(self, course):
        all_grades = {}
        for lecturer in self.lecturer_list:
            for k, v in lecturer.lecture_grades.items():
                if k == course:
                    if k not in all_grades.keys():
                        all_grades.setdefault(k, v)
                    else:
                        all_grades[k] = list(all_grades[k] + v)

        mean_all_grades = np.array(list(all_grades.values())).mean()
        print(f'\nСредняя оценка всех лекторов за курс "{course}": {mean_all_grades}')


# Создаем экземпляр: поток в Университете со своими студентами и лекторами, добавляем туда студентов и считаем среднюю оценку
# по классу Музыки и Питона
fall_12345 = University()
fall_12345.add_student(best_student)
fall_12345.add_student(second_best_student)
fall_12345.combine_grades_list('Music')
fall_12345.combine_grades_list('Python')

fall_12345.add_lecturer(wise_lecturer)
fall_12345.add_lecturer(evenwiser_lecturer)
fall_12345.lecturers_grades_list('Dance')