num = float(input("Enter your electric unit value = "))
bill = 0
if num <= 0:
    print(f"Invalid unit value (enter only positive number.).")
elif num <= 100:
    print(f"Your net bill = {bill}")
elif 100 < num <= 200:
    bill = bill + 100
else:
    bill = (num - 200) * 8 + 100
    print(f"The total amount = {bill}")