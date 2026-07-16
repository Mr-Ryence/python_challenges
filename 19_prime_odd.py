num=int(input("Enter any number = "))
if(num<=1):
     print(f"This is not a prime number.")
else: 
     for i in range(2, int(num**0.5)+1, 1):
          if num % i == 0:
               print(f"{num} is a not a prime number.")
               break
          else:
               print(f"This is a prime number.")