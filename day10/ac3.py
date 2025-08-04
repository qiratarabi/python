num = int(input("Enter a number"))
digit = len(str(num))
sum = 0
temp = num
while temp > 0:
    rem = temp % 10
    print("Remainder: ",rem)
    sum += rem ** digit 
    temp = temp//10
    print(("Temp: ",temp))
if sum == num:
    print("Armstrong number")
else:
    print("Not an armstrong number")
