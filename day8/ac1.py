attendance = int(input("Enter the student attendance"))
medical_condition = input("Do you have a medical cause Y or N")

if attendance >= 75:
    print("You are eligible to sit in the Exams")
else:
    if medical_condition == 'Y':
     print("You are allowed to sit in the examination")
    else:
     print("No you are not allowed to sit in the Exam")
