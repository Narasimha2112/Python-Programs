students = {}

n = int(input("Enter Number of Students: "))

for i in range(n):
    print(f"\n Enter Student {i+1}: ")
    
    name = input("Enter Student Name: ")
    
    total = 0
    marks = []
    for j in range(5):
        mark = int(input("Enter mark for subject {j+1}: "))
        marks.append(mark)
        total += mark
    
    grade = input("Enter Grade: ")
    
    students[name] = {
        "marks": marks,
        "grade": (grade,),
        "total": total
    }

min_total = float('inf')
max_total = float('-inf')

min_students = []
max_students = []

for name in students:
    
    total = 0
    for mark in students[name][marks]:
        total += mark
        
    
    if total < min_total:
        min_total = total
        min_students = [name]
    elif total == min_total:
        min_students.append(name)
    
    if total > max_total:
        max_total = total
        max_students = [name]
    elif total == max_total:
        max_students.append(name)

print("\n-----RESULT-----")
print("Minimum Total Marks:", min_total)
print("Student(s) with Minimum Marks:", min_students)

print("Maximum Total Marks:", max_total)
print("Student(s) with Maximum Marks:", max_students)