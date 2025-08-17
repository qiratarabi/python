n = int(input("Enter the number of rows you want"))
row  = n
column = n
count = 1
for i in range(0, row):
    for j in range(0, i+1):
        print(count, end = " ")
        count = count + 2
    print()