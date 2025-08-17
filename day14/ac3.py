def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1/num2

print("Please enter the operation")
print("1.Add")
print("2.Sub")
print("3.Mul")
print("4.Div")
choice = int(input("Enter your choice digit:"))
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
if choice == 1:
    answer = add(num1, num2)
    print("Sum = ", answer)
elif choice == 2:
    answer = sub(num1, num2)
    print("Sub = ",answer)
elif choice == 3:
    answer = mul(num1, num2)
    print("Mul = ",answer)
elif choice == 4:
    answer = div(num1, num2)
    print("Div = ",answer)
else:
    print("Invalid choice pleaseenter anything between 1-4")
