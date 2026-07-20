num=int(input("Enter the numbet between 1 to 999 = "))
count=0
if(num<=0 or num>1000):
     print(f"Please enter only 1-999 number.")
else: 
     while(num>0):
          count=count+1
          num=num//10
     print(f"The total number of digit is = {count}")