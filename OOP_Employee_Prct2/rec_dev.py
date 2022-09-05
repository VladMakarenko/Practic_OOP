from employee import Employee


class Recruiter(Employee):
    position = 'Recruiter'

    def __init__(self, first_name: str, salary_day: int):
        super().__init__(first_name, salary_day)

    def __str__(self):
        return f'{__class__.__name__}: {self.first_name}'

    @staticmethod
    def work():
        return 'I come to the office and start to hiring\n'


class Developer(Employee):
    position = 'Developer'

    def __init__(self, first_name: str, salary_day: int, tech_stack):
        super().__init__(first_name, salary_day)
        self.tech_stack = tech_stack

    def __str__(self):
        return f'{__class__.__name__}: {self.first_name}'

    @staticmethod
    def work():
        return 'I come to the office and start to coding\n'

    # first_name - повертає об'єднані імена двох екземплярів класу Develoepr
    # salary_day - порівнює ЗП двох екземплярів класу та повертає більшу
    # tech_stack - перевіряє списки двох екземплярів з навичками розброників
    # та повертає список з унікальними значеннями
    def __add__(self, other):
        return Developer(
            first_name=f'{self.first_name} {other.first_name}',
            salary_day=max(self.salary_day, other),
            tech_stack=list(set(self.tech_stack + other.tech_stack))
        )
