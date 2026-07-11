r=int(input("Enter the radius of the circle = "))
if(r>0):
     perimeter=2*(22/7)*r
     area=(22/7)*r*r
     print(f"The perimeter of the circle is {perimeter}")
     print(f"The area of the circle is {area}")
else: 
     print("please enter only positive numer")