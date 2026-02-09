Employees = {}

n = int(input("Enter Number of Employees: "))

for i in range(n):
    print(f"\n Enter Employee Detail {i+1}: ")
    
    name = input("Enter Employee Name: ")
    salary = int(input("Enter Salary: "))
    department = input("Enter Department: ")
    
    Employees[name] = {
        "salary": salary,
        "department": department
    }

min_salary = float('inf')
max_salary = float('-inf')

min_sal_employees = []
max_sal_employees = []

for employee in Employees:
    
    current_salary = Employees[employee]["salary"]
    
    if current_salary < min_salary:
        min_salary = current_salary
        min_sal_employees = [employee]
    elif salary == min_salary:
        min_sal_employees.append(employee)
    
    
    if current_salary > max_salary:
        max_salary = current_salary
        max_sal_employees = [employee]
    elif salary == max_salary:
        max_sal_employees.append(employee)
        
print(f"\n-----RESULT-----")
print("Highest Salary Employee(s):", max_sal_employees)
print("Salary:", max_salary)

print("Lowest Salary Employee(s):", min_sal_employees)
print("Salary:", min_salary)