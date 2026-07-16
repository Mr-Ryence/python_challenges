num=int(input("Enter the number where you want to add them = "))
sum=0
if(num<0):
     print(f"Please enter only positive number.")
else: 
     for i in range(1, num+1, 1):
          sum=sum+i
     print(f"The sum of 1 to {num} is = {sum}")
