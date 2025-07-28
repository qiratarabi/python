units = int(input("Please enter number of units you consumed"))
if units < 50:
    amount = units * 4
    discount = 25
elif units <= 100:
    amount = units * 4.5
    discount = 30
elif units <= 200:
    amount = units * 5
    discount =  35
else:
    amount = units * 7
    discount = 200
total = amount - discount
print("Electricity Bill: ",total)