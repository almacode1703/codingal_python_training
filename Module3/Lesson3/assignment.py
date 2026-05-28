def calculate_change(total_bill, amount_paid):
    return amount_paid - total_bill


bill = 2.50
paid = 4.00

change = calculate_change(bill, paid)

print("Change returned =", change)