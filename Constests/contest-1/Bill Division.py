def bonAppetit(bill, k, b):
    # Write your code here
    bill.pop(k)
    total = sum(bill)
    b_actual = total/2
    if b == b_actual:
        print("Bon Appetit")
    else:
        print(int(b-b_actual))