try:
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter secondnumber"))
    result  =  num1/num2
    print("Results: ",result)

except ZeroDivisionError as ex:
    print("Exception: Zero Division")
except ValueError as ex:
    print("Exception: ",ex)
except:
    print("Exception: Something went wrong")
else:
    print("No exception")
finally:
    print("i will always excecute")
