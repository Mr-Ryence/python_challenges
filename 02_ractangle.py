l=int(input("Enter the length of rectangle: "))
b=int(input("Enter the breath of rectangle: "))
if (l>0 and b>0): 
     perimeter=2*(l+b)
     area=l*b
     print(f"The perimeter of the rectangle is {perimeter}")
     print(f"The area of the rectangle is {area}")
else: 
     print("Please enter only positive value.")
     