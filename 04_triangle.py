b=int(input("Enter the base of the triangle = "))
h=int(input("Enter the height of the triangle = "))
if(b>0 and h>0): 
     area=1/2*(b*h)
     print(f"The area of the trianlge is {area}")
else: 
     print("please enter only positive number.")