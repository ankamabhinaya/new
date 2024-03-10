#Simple Calculator
print("1.Addition")
print("2.Subtraction")
print("3.Multiply")
print("4.Division")

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

num=int(input("Enter the operation: "))
if num ==1 :
  print(a+b)
elif num == 2:
  print(a-b)
elif num == 3:
  print(a*b)
elif num == 4:
  print(a/b)
else:
  print("invalid Operation")