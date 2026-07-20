# WAP in python to print the cube the number between 10-15
s=int(input("Enter the start range value = "))
l=int(input("Enter the last range value = "))
for i in range(s, l+1, 1):
    print(f"{i}*{i}*{i} = {i**3}")
     