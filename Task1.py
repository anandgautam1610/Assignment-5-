student = {
    "Alice" : 85,
    "Anand" : 100,
    "Sakshi" : 99,
    "Harsh" : 87,
}
try:
    a =  input("Enter the student's name : ")
    a_ = a.strip()
    print(f"{a_}'s marks's :  {student[a_]}")
except:
    print("Student not found.")