import math
a=int(input("Enter the first side = "))
b=int(input("Enter the second side = "))
c=int(input("Enter the third side = "))
if(a>0 and b>0 and c>0):
     if(a+b>c and a+c>b and b+c>a): 
          s=(a+b+c)/2
          area=math.sqrt((s*(s-a)*(s-b)*(s-c)))
          print(f"The area of the trangle is {area}")
     else: 
          print("This is not follow the pythagorus theorem.")
else: 
     print("please enter only positive number.");