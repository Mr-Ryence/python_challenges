f=int(input("Enter the first number = "))
s=int(input("Enter the second number = "))
t=int(input("Enter the third number = "))
fo=int(input("Enter the fourth number = "))
fi=int(input("Enter the fivth number = "))
if(f<=0 and s<=0 and t<=0 and fo<=0 and fi<=0):
     print(f"Invalid unput")
else: 
     avg=(f+s+t+fo+fi)/5
print(f"The average value = {avg}")
