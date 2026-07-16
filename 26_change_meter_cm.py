km=float(input("Enter the meter value = "))
if(km<=0):
     print(f"Please enter only positive number.")
else:
     m=(km*1000)
     cm=(m*100)
     print(f"{km} kilometer= {m} meter")
     print(f"{m} meter= {cm} centemeter")
