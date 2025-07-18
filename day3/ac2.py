amount = int(input("please enter amount for wthdraw"))
note100 = amount // 100 
remaining_amount = amount % 100
note50 = remaining_amount // 50
remaining_amount = amount % 50 
note10 = remaining_amount // 10 

print("note of 100 rupee: ",note100)
print("note of 50 rupee: ",note50)
print("note of 10 rupee",note10)
