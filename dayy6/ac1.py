age = int(input("Enter your age"))
if(type(age) is int):
  print("Age is valid")
else:
  print("Age is not valid")

amount = float(input("Enter your amount"))
if(type(amount) is float):
  print("Amount is valid")
else:
  print("Amount not valid")

name = "Qirat"
if(type(name) is not int):
  print("Its not an integer")

  a = 12
  b = 12
  if (a is b):
    print("a and b are equal")