num=int(input("Enter the number which you want to find cube = "))
if(num<0):
     print(f"Please enter only positive number.")
else: 
     result=pow(num, 3)
     print(f"The cube of {num} is = {result}")