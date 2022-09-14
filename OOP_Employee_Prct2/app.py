import traceback
from datetime import datetime

import employee
from employee import Employee
import rec_dev
from exception import EmailAlreadyExistsException
from candidates import *


# print(Employee.work())
#
# recruiter_ivanov = rec_dev.Recruiter('Ivanov', 1000)
# print(recruiter_ivanov)
# print(recruiter_ivanov.check_salary(2)) # підрахунок ЗП за 2 дні
# print(f'august salary - {recruiter_ivanov.data_check_salary(8)}_USD') # підрахунок ЗП з 1 числа 8 місяця (серпень)
# print(rec_dev.Recruiter.work())
#
# develop_petrov = rec_dev.Developer('Ivan', 2000, ['python', 'js', 'c#', 'Scratch'])
# print(develop_petrov)
# print(develop_petrov.check_salary(30)) # підрахунок ЗП за 30 днів
# print(f'august salary - {develop_petrov.data_check_salary(8)}_USD')# підрахунок ЗП з 1 числа 8 місяця (серпень)
# print(rec_dev.Developer.work())
#
# develop_stepanov = rec_dev.Developer('Stepan', 300, ['python', 'pascal', 'c++', 'Fortran', 'Scratch'])
#
# # порівняння ЗП
# print(
#     f'Salary {recruiter_ivanov.first_name} more than {develop_petrov.first_name}!'
#     if recruiter_ivanov > develop_petrov and recruiter_ivanov != develop_petrov
#     else f'Salary {recruiter_ivanov.first_name} less than {develop_petrov.first_name}!'
# )
#
# print(develop_petrov.tech_stack < develop_stepanov.tech_stack)
#
# print((develop_petrov+develop_stepanov).__dict__)


def main():
    shevchenko = Employee('asd', 100, 'shevchenko@gmai.com')
    print(shevchenko)

    petrenko = Employee('qwe', 100, 'petrenko@gmai.com')
    print(petrenko)


if __name__ == '__main__':
    try:
        main()
    except EmailAlreadyExistsException:
        log_message = f'{datetime.now()} \n {traceback.format_exc()}\n'
        with open('logs.txt', 'a+') as lf:
            lf.write(log_message)
    print('[=================================================================================================]')
if __name__ == '__main__':
    stepanov = Candidate('Stepan', 'Stepanov', 'stepka@gmail.com',
                                    ['Java', 'js', 'python'], 'python', 'middle')
    print(stepanov.__dict__)
    print('[=================================================================================================]')

    candidates = Candidate.generate_candidates('candidates.csv')
    [print(x.__dict__) for x in candidates]
    for x in candidates:
        print(x.get_full_name)
    print('[=================================================================================================]')

    candidates = Candidate.generate_candidates(
        'https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv'
    )
    [print(x.__dict__) for x in candidates]
    for x in candidates:
        print(x.get_full_name)
