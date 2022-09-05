from employee import Employee
import rec_dev


print(Employee.work())

recruiter_ivanov = rec_dev.Recruiter('Ivanov', 1000)
print(recruiter_ivanov)
print(recruiter_ivanov.check_salary(2)) # підрахунок ЗП за 2 дні
print(f'august salary - {recruiter_ivanov.data_check_salary(8)}_USD') # підрахунок ЗП з 1 числа 8 місяця (серпень)
print(rec_dev.Recruiter.work())

develop_petrov = rec_dev.Developer('Ivan', 2000, ['python', 'js', 'c#', 'Scratch'])
print(develop_petrov)
print(develop_petrov.check_salary(30)) # підрахунок ЗП за 30 днів
print(f'august salary - {develop_petrov.data_check_salary(8)}_USD')# підрахунок ЗП з 1 числа 8 місяця (серпень)
print(rec_dev.Developer.work())

develop_stepanov = rec_dev.Developer('Stepan', 300, ['python', 'pascal', 'c++', 'Fortran', 'Scratch'])

# порівняння ЗП
print(
    f'Salary {recruiter_ivanov.first_name} more than {develop_petrov.first_name}!'
    if recruiter_ivanov > develop_petrov and recruiter_ivanov != develop_petrov
    else f'Salary {recruiter_ivanov.first_name} less than {develop_petrov.first_name}!'
)

print(develop_petrov.tech_stack < develop_stepanov.tech_stack)

print((develop_petrov+develop_stepanov).__dict__)