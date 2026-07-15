num=int(input("Enter any number = "))
count=0
if(num<=0):
     print("Please enter only positive number.")
else: 
     while(num>0):
          num%10
          count+=1
          num=num//10
     print(f"There are {count} digit in this number.")
     