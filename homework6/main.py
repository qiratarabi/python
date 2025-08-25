try:
    age = int(input("Enter your age"))
    print("the age entered is ",age)
except ValueError as ex:
    print("invalid")
    