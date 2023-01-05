n = int(input('Enter the number of employees:'))
employees = {}
for i in range (n):
    name = input('Enter Employee Name :')
    salary = input('Enter Employee Salary:')
    employees[name]=salary
print('You can know the salary details by entering the name')
while True:
    name = input('Enter Employee Name:')
    salary = employees.get(name, -1)
    if salary == -1:    
        print("Employee does not exist")
    else:
        print('The Salary of the employee is:',salary)
    choice = input('Do you want to know the salary of an other employee[Yes|No]')
    if choice == 'No':
        break