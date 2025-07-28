a = int(input("Enter first value"))
b = int(input("Enter second value"))
c = int(input("Enter third value"))
avg = (a + b + c) / 3
print("Avg: ",avg)
if avg > a and avg > b and avg > c:
    print("Average is greater than all")
elif avg > a and avg > b:
    print("Average is greater than a and b")
elif avg > a and avg > c:
    print("Average is greater than a and c")  
elif avg > b and avg > c:   
    print("Average is greater than b and c")
else:
    print("Average is not greater than all")










