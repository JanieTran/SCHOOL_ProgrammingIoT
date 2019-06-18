# TUTORIAL 2
# Exercise 2 - Object-oriented Python
#
# Student Name: Tran Thi Hong Phuong
# Student ID: s3623386

# =============================================================
# Course class
# =============================================================


class Course:
    id = ''
    teacher = ''
    n_enrolled = 0
    max_students = 10
    charge_per_student = 0
    students_list = []
    income = 0
    cost = 0

    def get_info(self):
        print('Course ID:', self.id)
        print('Teacher:', self.teacher)
        print('Number of enrolled students:', self.n_enrolled)
        print('Maximum number of students:', self.max_students)
        print('Charge per student:', self.charge_per_student)
        print('List of students:', self.students_list)
        print('Income:', self.income)
        print('Cost:', self.cost)
        print()


# =============================================================
# Cooking courses
# =============================================================

class Cooking(Course):
    def __init__(self):
        self.cost = 1000


class ItalianCooking(Cooking):
    def __init__(self):
        super().__init__()
        self.id = '001'
        self.charge_per_student = 500
        self.get_info()


class Seafood(Cooking):
    def __init__(self):
        super().__init__()
        self.id = '002'
        self.charge_per_student = 700
        self.get_info()


# =============================================================
# Sewing courses
# =============================================================

class Sewing(Course):
    def __init__(self):
        self.id = '003'
        self.charge_per_student = 300
        self.cost = 100 * self.n_enrolled
        self.get_info()


# =============================================================
# Writing courses
# =============================================================

class Writing(Course):
    def __init__(self):
        self.charge_per_student = 200
        self.max_students = 15


class Creative(Writing):
    def __init__(self):
        super().__init__()
        self.id = '004'
        self.get_info()


class Business(Writing):
    def __init__(self):
        super().__init__()
        self.id = '005'
        self.get_info()


# =============================================================
# Instances
# =============================================================

print('---ITALIAN COOKING---')
italian = ItalianCooking()
print('---SEAFOOD---')
seafood = Seafood()
print('---SEWING---')
sewing = Sewing()
print('---CREATIVE---')
creative = Creative()
print('---BUSINESS---')
business = Business()
