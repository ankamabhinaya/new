
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))

if a > b:
  if a > c:
    print( a," is greater")
  else:
    print(c ," is greater")
else:
  if b > c:
    print(b ," is greater")
  else:
    print(c ," is greater")


#          (or)


a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
if a>b and a>c:
  print(a," is greater")
elif b>a and b>c:
  print(b," is greater")
else:
  print(c," is greater")
 


