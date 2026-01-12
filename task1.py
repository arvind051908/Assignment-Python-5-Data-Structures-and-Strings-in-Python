# Task 1: Create a Dictionary of Student Marks
student = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,}

name = input("Enter the student's name: ")

if name in student:
    print(name,"Marks:", student[name])
else:    
    print("student not found")


 
