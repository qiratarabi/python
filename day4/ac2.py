purchase_amount = float(input("Please enter purchase"))
selling_amount = float(input("Please enter selling amount"))
profit = selling_amount - purchase_amount
if profit > 0:
    print("You made a profit")
elif profit < 0:
    print("You made a loss")
else:
    print("No profit no loss")