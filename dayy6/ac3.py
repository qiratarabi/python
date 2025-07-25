english = int(input("Enter marks in English"))
maths = int(input("Enter marks in Maths"))
science = int(input("Enter marks in Science"))
urdu = int(input("Enter marks in Urdu"))
avg = (english + maths + science + urdu)

if avg > 90:
    print("Grade A")
elif avg > 80:
    print("Grade B")
elif avg > 60:
    print("Grade C")
else:
    print("Grade D")