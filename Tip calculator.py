bill = int(input("What's your bill?: "))
tip = int(input("Whow many persent do you want to tip?: "))
tip_persentage = (tip / 100)*bill 
total_bill = tip_persentage + bill
print(f"Your bill is {bill} and you want to give tip {tip}%. So your total bill is {total_bill}")