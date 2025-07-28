print("select your ride")
print("1. Bike")
print("2. Car")
choice = int(input("Enter your choice 1 or 2"))
if choice == 1:
    print("What bike do you want")
    print("1. scooty")
    print("2. motorbike")
    choice = int(input("Enter which one 1 or 2"))
    if choice == 1:
        print("You are riding a scooty")
    else:
        print("You are riding a motorbike")           
if choice == 2:
    print("Which car do you want")
    print("1. SUV")
    print("2. Sedan")
    choice = int(input("Enter which one 1 or 2"))
    if choice == 1:
      print("You are riding SUV")
    else:
      print("You are ridinga Sedan")
