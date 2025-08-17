n = int(input("Enter the number of rows of star you want to print"))
row = n 
column = n 
for i in range(0, row):
 for j in range(0, i+1):
   print("*",end = "")
 print()