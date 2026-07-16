p=float(input("Enter the principal value = "))
r=float(input("Enter the rate = "))
t=float(input("Enter the time in year = "))
if(p<=0):
     print(f"Invalid principal value.")
elif(t<=0):
     print (f"Invalid time value.")
elif(r<0):
     print(f"Please enter the correct rate value.")    
else: 
     i=(p*r*t)/100
     si=p+i
     print(f"The principal amount is = {p}")
     print(f"The total interest is = {i}")
     print(f"The total amount  is = {si}")