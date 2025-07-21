a = 10 
b = 12
c = 12

print(a != b) #True
print(b != c) #False

a = "python"
b = "qirat"
if a != b:
    print("Both strings are not equal")
else:
    print("Both are Equal")

if (a == 10) != (b == 12):
    print("End")a = 10 #True
b = 12 #True
c = 0 #False
if a and b and c:
    print("All the numbers have boolean valuse as True")
else:
    print("Atleast one of number have boolean value False")

    a = 10
    b = -10
    c = 0
    if a > b and c > b:
        print("Happy")
    else:
        print("Unhappy")