def total_calc(bill_amount, tip_perc):
    total_amount = bill_amount + (bill_amount * tip_perc)
    total = round(total_amount, 2)
    print(f"please pay $ {total}")

bill_amount = float(input("Enter the bill amount"))
tip_perc = float(input("Enter the tip percentage"))
total_calc(bill_amount, tip_perc)