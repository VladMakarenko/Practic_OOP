from datetime import date, datetime

import numpy as np


class Employee:
    def __init__(self, first_name: str, last_name: str, salary_day: int):
        self.first_name = first_name
        self.last_name = last_name
        self.salary_day = salary_day

    @staticmethod
    def work():
        return 'I come to the office\n'

    def __call__(self):
        return self.salary_day

    def __lt__(self, other):
        return self() < other

    def __le__(self, other):
        return self() <= other

    def __eq__(self, other):
        return self() == other

    def __ne__(self, other):
        return self() != other

    def __gt__(self, other):
        return self() > other

    def __ge__(self, other):
        return self() >= other

    def check_salary(self, days: int):
        return self.salary_day * days

    def data_check_salary(self, month):
        d1 = date(2022, month, 1)
        d2 = datetime.now()
        work_day = np.busday_count(d1.strftime("%Y-%m-%d"), d2.strftime("%Y-%m-%d"))
        work_day = work_day + 1
        salary_working_day = self.salary_day * work_day
        return salary_working_day


class Recruiter(Employee):
    position = 'Recruiter'

    def __str__(self):
        return f'{self.position}: {self.first_name}'

    @staticmethod
    def work():
        return 'I come to the office and start to hiring\n'


class Developer(Employee):
    position = 'Developer'

    def __init__(self, first_name: str, last_name: str, salary_day: int, tech_stack: list):
        super().__init__(first_name, last_name, salary_day)
        self.tech_stack = tech_stack

    def __str__(self):
        return f'{self.position}: {self.first_name}'

    @staticmethod
    def work():
        return 'I come to the office and start to coding\n'


if __name__ == '__main__':
    print(Employee.work())

    recruiter_ivanov = Recruiter('Ivanov', 'Petro', 1000)
    print(recruiter_ivanov)
    print(recruiter_ivanov.check_salary(2))
    print(f'august salary - {recruiter_ivanov.data_check_salary(9)}_USD')
    print(Recruiter.work())

    develop_petrov = Developer('Petrov', 'Ivan', 2000, ['python', 'js', 'c#', 'Scratch'])
    print(develop_petrov)
    print(develop_petrov.check_salary(30))
    print(f'august salary - {develop_petrov.data_check_salary(9)}_USD')
    print(Developer.work())

    develop_stepanov = Developer('Stepanov', 'Stepan', 300, ['python', 'pascal', 'c++', 'Fortran', 'Scratch'])

    print(
        f'Salary {recruiter_ivanov.first_name} more than {develop_petrov.first_name}!'
        if recruiter_ivanov > develop_petrov and recruiter_ivanov != develop_petrov
        else f'Salary {recruiter_ivanov.first_name} less than {develop_petrov.first_name}!'
    )

    print({len(develop_petrov.tech_stack) <= len(develop_stepanov.tech_stack)})

    adding_class_objects = f'{develop_petrov.first_name} {develop_stepanov.first_name},' \
                           f' unique values: {list(set(develop_petrov.tech_stack + develop_stepanov.tech_stack))},' \
                           f' max salary: {max(develop_petrov.salary_day, develop_stepanov.salary_day)}'
    print(adding_class_objects)
