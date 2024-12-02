Amount = float(input("Enter the amount for which to calculate interest"))
Rate = float(input("enter the rate at which amount gains interest"))
Time = int(input("Enter the duration for which interest is to be calculated"))
interest = 0
profit = 0

while Time > 0:
    interest = Amount * Rate
    Amount = Amount + interest
    profit = profit + interest
    Time -= 1
print(f"Your balance is {Amount} and you money gained an interest of {profit}")
