num=int(input("Enter the number which you want to find factorial = "))
fact=1
if(num<=0):
     print(f"Please enter only positive number.")
else: 
     for i in range(1, num+1, 1):
          fact=fact*i
print(f"The factorial of {num} is {fact}")