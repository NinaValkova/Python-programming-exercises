line = input()

company_employee = {}
while line != 'End':
    command = line.split(' -> ')
    
    company = command[0]
    employee = command[1]
    
    if company not in company_employee:
        company_employee[company] = [employee]
    elif employee not in company_employee[company]:
        company_employee[company].append(employee)   
    
    line = input()    

for company, employee in  company_employee.items():
    print(f'{company}')
    size = len(employee)
    for i in range(0, size, 1):
        print(f'-- {employee[i]}')      