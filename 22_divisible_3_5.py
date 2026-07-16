num=int(input("Enter any number = "))
if(num<=0):
     print(f"Please enter only positive number.")
elif(num%3==0 and num%5==0): 
     print(f"This is divisible by 3 and 5.")
else: 
     print(f"This is not divisible by 3 and 5.")