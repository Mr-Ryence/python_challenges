num=int(input("Enter any number = "))
newNum=num
reverse=0
while(num>0):
     digit=num%10
     reverse=reverse*10+digit
     num=num//10
if(newNum==reverse):
     print(f"This is a pelindrum number.")
else: 
     print(f"This is not a pelindrum number.")
          