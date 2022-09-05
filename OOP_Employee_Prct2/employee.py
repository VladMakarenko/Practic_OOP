from datetime import date, datetime

import numpy as np


class Employee:
    def __init__(self, first_name: str, salary_day: int):
        self.first_name = first_name
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

    # рахує ЗП за вказану кількість днів
    def check_salary(self, days: int):
        return self.salary_day * days

    # рахує ЗП з 1 числа вказаного місяця по поточну дату
    def data_check_salary(self, month):
        d1 = date(2022, month, 1)
        d2 = datetime.now()
        work_day = np.busday_count(d1.strftime("%Y-%m-%d"), d2.strftime("%Y-%m-%d"))
        work_day = work_day + 1
        salary_working_day = self.salary_day * work_day
        return salary_working_day
